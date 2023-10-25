from manim import *
import numpy as np
from manim.utils.unit import Percent, Pixels
# Goal is to show the how a missing point on a circle can be filled by moving points around the circle infinitley
# manim -pql Filling_Circle.py

class Filling_Circle(Scene):
    def construct(self):
        plane = NumberPlane()
        #self.add(plane)


        c = Circle(color=WHITE, radius=3)
        hole = Dot(point=3*UP, radius=0.08, color=BLACK)
        # The circumference is irrational
        rad_circ = MathTex(r'C = 2 \pi r')

        starting_points= VGroup(
            Dot(point=plane.coords_to_point(3*np.cos(2*57.2958*DEGREES),3*np.sin(2*57.2958*DEGREES)), color=RED),
            Dot(point=plane.coords_to_point(3*np.cos(3*57.2958*DEGREES),3*np.sin(3*57.2958*DEGREES)), color=BLUE),
            Dot(point=plane.coords_to_point(3*np.cos(4*57.2958*DEGREES),3*np.sin(4*57.2958*DEGREES)), color=GREEN),
            Dot(point=plane.coords_to_point(3*np.cos(5*57.2958*DEGREES),3*np.sin(5*57.2958*DEGREES)), color=YELLOW),
            Dot(point=plane.coords_to_point(3*np.cos(6*57.2958*DEGREES),3*np.sin(6*57.2958*DEGREES)), color=GOLD),
            Dot(point=plane.coords_to_point(3*np.cos(7*57.2958*DEGREES),3*np.sin(7*57.2958*DEGREES)), color=MAROON),
            Dot(point=plane.coords_to_point(3*np.cos(8*57.2958*DEGREES),3*np.sin(8*57.2958*DEGREES)), color=PURPLE),
            Dot(point=plane.coords_to_point(3*np.cos(9*57.2958*DEGREES),3*np.sin(9*57.2958*DEGREES)), color=PINK),
            Dot(point=plane.coords_to_point(3*np.cos(10*57.2958*DEGREES),3*np.sin(10*57.2958*DEGREES)), color=ORANGE),
            Dot(point=plane.coords_to_point(3*np.cos(11*57.2958*DEGREES),3*np.sin(11*57.2958*DEGREES)), color=DARK_BROWN),
            Dot(point=plane.coords_to_point(3*np.cos(12*57.2958*DEGREES),3*np.sin(12*57.2958*DEGREES)), color=WHITE),
            Dot(point=plane.coords_to_point(3*np.cos(13*57.2958*DEGREES),3*np.sin(13*57.2958*DEGREES)), color=DARK_GRAY)
        )

        end_points= VGroup(
            Dot(point=3*UP, color=RED),
            Dot(point=plane.coords_to_point(3*np.cos(2*57.2958*DEGREES),3*np.sin(2*57.2958*DEGREES)), color=RED),
            Dot(point=plane.coords_to_point(3*np.cos(3*57.2958*DEGREES),3*np.sin(3*57.2958*DEGREES)), color=BLUE),
            Dot(point=plane.coords_to_point(3*np.cos(4*57.2958*DEGREES),3*np.sin(4*57.2958*DEGREES)), color=GREEN),
            Dot(point=plane.coords_to_point(3*np.cos(5*57.2958*DEGREES),3*np.sin(5*57.2958*DEGREES)), color=YELLOW),
            Dot(point=plane.coords_to_point(3*np.cos(6*57.2958*DEGREES),3*np.sin(6*57.2958*DEGREES)), color=GOLD),
            Dot(point=plane.coords_to_point(3*np.cos(7*57.2958*DEGREES),3*np.sin(7*57.2958*DEGREES)), color=MAROON),
            Dot(point=plane.coords_to_point(3*np.cos(8*57.2958*DEGREES),3*np.sin(8*57.2958*DEGREES)), color=PURPLE),
            Dot(point=plane.coords_to_point(3*np.cos(9*57.2958*DEGREES),3*np.sin(9*57.2958*DEGREES)), color=PINK),
            Dot(point=plane.coords_to_point(3*np.cos(10*57.2958*DEGREES),3*np.sin(10*57.2958*DEGREES)), color=ORANGE),
            Dot(point=plane.coords_to_point(3*np.cos(11*57.2958*DEGREES),3*np.sin(11*57.2958*DEGREES)), color=DARK_BROWN),
            Dot(point=plane.coords_to_point(3*np.cos(12*57.2958*DEGREES),3*np.sin(12*57.2958*DEGREES)), color=WHITE)
        )

        for dot in starting_points:
            self.add(TracedPath(dot.get_center,stroke_opacity = 0))

        self.play(Write(c))
        self.play(FadeIn(hole), Flash(hole), lag_ratio = 1)
        self.wait()
        self.play(Write(rad_circ))
        self.wait()
        self.play(Write(starting_points, lag_ratio=1), run_time=6)
        self.wait(5)
        self.play(
            Transform(
                starting_points,
                end_points,
                path_func=utils.paths.path_along_arc(-57.2958*DEGREES),
                run_time=10,
                lag_ratio = 1
            )
        )
        self.remove(hole)
        self.play(Flash(c, run_time=2, line_length=1,time_width=0.3,flash_radius=3 + SMALL_BUFF, rate_func = rush_from), FadeOut(starting_points, run_time=0.1))
        self.wait(5)
        
