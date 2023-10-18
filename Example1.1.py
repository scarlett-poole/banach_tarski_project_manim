from manim import *
import numpy as np
# Goal is to show the action of SO3 on a point x on the hollow unit sphere
# manim -pql project.py "Class Name"

class Example_1_1(ThreeDScene):
    # Parametric sphere
    def func(self, u, v):
        return np.array([np.sin(u) * np.cos(v), np.sin(u) * np.sin(v), np.cos(u)])

    def construct(self):
        # Define axes
        axes = ThreeDAxes(
            x_range=[-2,2], 
            x_length=4,
            y_range=[-2,2],
            y_length=4,
            z_range=[-2,2],
            z_length=4
        )

        # Define axis labels
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Define sphere
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[0, np.pi],
            v_range=[0, 2*np.pi],
            resolution=30,
            fill_opacity=0.75,
            checkerboard_colors=False,
            fill_color=GRAY,
            stroke_opacity=0
        )

        # Set camera angle
        self.move_camera(phi=70 * DEGREES, theta=45 * DEGREES)

        # Set scale of sphere, axes and labels
        self.add(surface.scale(1.2), axes.scale(1.2), labels.scale(1.2))
        self.remove(surface.scale(1.2), axes.scale(1.2), labels.scale(1.2))

        # Add axes and sphere
        self.play(FadeIn(axes), FadeIn(labels), Write(surface), run_time=0.5)

        # Move sphere and axes to right of frame
        self.play(surface.animate.shift(1.1*OUT), axes.animate.shift(1.1*OUT), labels.animate.shift(1.1*OUT), run_time = 0.5)

        # Define text for x
        x = MathTex(r'x = \begin{pmatrix}1\\0\\0\end{pmatrix}').to_corner(DOWN + LEFT)
        # Define text for action
        A_act_x = MathTex(r'A \triangleright x =\begin{pmatrix}0 & -1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}\begin{pmatrix}1\\0\\0\end{pmatrix}').to_corner(DOWN + LEFT)
        # Define text for x_1
        x_1 = MathTex(r'= \begin{pmatrix}0\\1\\0\end{pmatrix} = x_1 \in \mathbb{S}^2').align_to(A_act_x, RIGHT).shift((4*RIGHT + 2.6*DOWN))

        # Define x
        start_point = Dot3D(point=axes.coords_to_point(1, 0, 0), color=PURE_RED)

        # Define x_1
        end_point = Dot3D(point=axes.coords_to_point(0,1,0), color=PURE_RED)

        # Define circle centre
        circle_center = Dot3D(point=axes.coords_to_point(0, 0, 0), fill_opacity = 0, stroke_opacity=0)

        # Add path for Transform
        self.add(
            TracedPath(
                start_point.get_center, 
                stroke_color=start_point.get_color(),
                dissipating_time=0.8, 
                stroke_opacity=[0, 1]
            )
        )

        # Add Transform circle centre
        self.add(circle_center)

        # Fix text for x in frame
        self.add_fixed_in_frame_mobjects(x)
        self.remove(x)
        # Fix text for A acting on x in frame
        self.add_fixed_in_frame_mobjects(A_act_x)
        self.remove(A_act_x)
        # Fix text for x_1 in frame
        self.add_fixed_in_frame_mobjects(x_1)
        self.remove(x_1)

        # Play x and text for x
        self.play(Write(x),FadeIn(start_point))
        self.play(Flash(start_point), Indicate(x))
        self.play(Unwrite(x))
        self.wait(0.5)

        # Play A acting on x
        self.play(Write(A_act_x), run_time = 0.5)
        
        # Move x to x_1 and write x_1
        self.play(Transform(start_point,end_point,path_func=utils.paths.path_along_circles(PI/2, circle_center.get_center()),run_time=2))
        
        # Play text for x_1
        self.play(Write(x_1))
        self.play(Flash(end_point), Indicate(x_1))
        self.wait(2)