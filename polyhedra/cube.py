from manim import *

class CubeExpl(ThreeDScene):

    def construct(self):
        cube = Cube().scale(3/2).rotate(60 * DEGREES).rotate(-60 * DEGREES, axis=[0, 1, 0])
        self.play(DrawBorderThenFill(cube))
        scr_height = config["frame_height"] / 4
        dots = VGroup(
            Dot([-scr_height, scr_height, 0]).set_color(YELLOW),
            Dot([scr_height, scr_height, 0]),
            Dot([scr_height, -scr_height, 0]),
            Dot([-scr_height, -scr_height, 0]),
            Dot([2 * scr_height, 1.5 * scr_height, 0]),
            Dot([-2 * scr_height, 1.5 * scr_height, 0]),
            Dot([2 * scr_height, -1.5 * scr_height, 0]),
            Dot([-2 * scr_height, -1.5 * scr_height, 0]),
        )
        lines = VGroup(
            Line(dots[0], dots[1]),
            Line(dots[1], dots[2]),
            Line(dots[2], dots[3]),
            Line(dots[3], dots[0]),
            Line(dots[1], dots[4]),
            Line(dots[0], dots[5]),
            Line(dots[3], dots[7]),
            Line(dots[2], dots[6]),
            Line(dots[4], dots[5]),
            Line(dots[5], dots[7]),
            Line(dots[7], dots[6]),
            Line(dots[6], dots[4]),
        )
        grp = VGroup(*lines, *dots)
        self.play(Unwrite(cube))
        self.play(Write(grp))
        self.play(grp.animate.shift(2 * LEFT))
        
        edges_label = Text("Edges: 12").set_color(BLUE).move_to(RIGHT * 4)
        faces_label = Text("Faces: 6").set_color(RED).next_to(edges_label, 1.25 * UP)
        vertices_label = Text("Vertices: 8").set_color(YELLOW).next_to(edges_label, 1.25 * DOWN)

        self.play(Write(VGroup(edges_label, faces_label, vertices_label)))


