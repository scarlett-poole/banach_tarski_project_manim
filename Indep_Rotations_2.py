from manim import *
import numpy as np
# Goal is to show the action of a subgroup of SO3 acting on S^2. 
# For slide: Theorem: SO3 is Paradoxical
# manim -pql Indep_Rotations_2.py 

class Indep_Rotations_2(ThreeDScene):
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
            fill_color=GRAY,
            checkerboard_colors=False,
            stroke_opacity=0.5
        )

        # Set camera angle
        self.move_camera(phi=70 * DEGREES, theta=45 * DEGREES)

        # Set scale of sphere, axes and labels
        self.add(surface.scale(1.3), axes.scale(1.3), labels.scale(1.3))
        self.remove(surface.scale(1.3), axes.scale(1.3), labels.scale(1.3))

        # Define A(rotation counter clockwise about z axis) & B(rotation counterclockwise about x axis) matrices
        Mat_A = MathTex(r'A =\begin{pmatrix}\frac{1}{3} & -\frac{2\sqrt{2}}{3} & 0\\\frac{2\sqrt{2}}{3} & \frac{1}{3} & 0\\0 & 0 & 1\end{pmatrix}').scale(0.7).to_corner(DOWN + LEFT)
        Mat_B = MathTex(r'B =\begin{pmatrix}1 & 0 & 0\\0 & \frac{1}{3} & -\frac{2\sqrt{2}}{3}\\0 & \frac{2\sqrt{2}}{3} & \frac{1}{3}\end{pmatrix}').scale(0.7).to_corner(DOWN + LEFT)

        # Define start point for A rotation
        start_point_A = Dot3D(point=axes.coords_to_point(1, 0, 0), color=PURE_RED)
        # Define start point for B rotation
        start_point_B = Dot3D(point=axes.coords_to_point(0, 0, 1), color=PURE_RED)

        grp = VGroup(surface, start_point_A, start_point_B)

        # Fix A & B Matrices in frame
        self.add_fixed_in_frame_mobjects(Mat_A)
        self.remove(Mat_A)
        self.add_fixed_in_frame_mobjects(Mat_B)
        self.remove(Mat_B)

        # Add axes and sphere
        self.play(FadeIn(axes), FadeIn(labels), Write(grp), run_time=0.5)
        self.wait(1)
        #self.begin_ambient_camera_rotation(rate=0.4)

        # Play matrix A & point
        self.play(Write(Mat_A), run_time = 0.5)
        self.wait(1)

        # Rotate sphere & point with A(rotation counter clockwise about z axis)
        self.play(Rotate(grp, np.arccos(1/3), OUT),run_time=3)
        self.play(Rotate(grp, -np.arccos(1/3), OUT),run_time=1)
        self.wait(1)

        # Remove matrix A, Play matrix B
        self.play(Unwrite(Mat_A), run_time = 0.5)
        self.play(Write(Mat_B),run_time = 0.5)
        self.wait(1)

        # Rotate sphere with b(rotation counter clockwise about x axis)
        self.play(Rotate(grp, np.arccos(1/3), RIGHT),run_time=3)
        self.play(Rotate(grp, -np.arccos(1/3), RIGHT),run_time=1)
        self.wait(1)