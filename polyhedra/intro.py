from manim import *
from itertools import combinations

class Main(ThreeDScene):

    def construct(self):

        # Objects needed for the scene
        title_text = Text("Euler's formula for polyhedra")
        formula = MathTex("F", "-", "E", "+", "V", "= 2")
        f_expl = Text("Number of faces").set_color(RED)
        e_expl = Text("Number of edges").set_color(BLUE)
        v_expl = Text("Number of vertices").set_color(YELLOW)
        
        # Animation - introduce the formula
        self.play(Write(title_text))
        self.play(Unwrite(title_text))
        self.play(Write(formula))
        self.play(formula.animate.move_to(2.1 * UP).scale(3))

        # Animation - labels for the formula
        for idx, clr, obj, pos in zip((0, 2, 4), (RED, BLUE, YELLOW), (f_expl, e_expl, v_expl), (-2, -1, 0.05)):
            formula[idx].set_color(clr)
            self.play(Write(obj))
            self.play(obj.animate.move_to(pos * UP))

        self.play(FadeOut(f_expl, v_expl, e_expl))
        self.play(formula.animate.scale(0.3333).to_corner(UL))

        # Create cube and send to corner
        cube = Cube().scale(3/2).rotate(75 * DEGREES).rotate(-45 * DEGREES, axis=[0, 1, 0])
        self.play(DrawBorderThenFill(cube))
        self.play(cube.animate.scale(2/3).shift(4 * LEFT))

        # Labels - label the square's properties
        faces = Tex("Faces = ", "6").set_color(RED)
        edges = Tex("Edges = ", "12").set_color(BLUE)
        vertices = Tex("Vertices = ", "8").set_color(YELLOW)

        self.play(Write(faces))
        self.play(faces.animate.shift(1 * RIGHT + 1.5 * UP))

        self.play(Write(vertices))
        self.play(vertices.animate.shift(1 * RIGHT + 1.5 * DOWN))

        self.play(Write(edges))
        self.play(edges.animate.shift(1 * RIGHT))

        minus, plus, number = MathTex("-"), MathTex("+"), MathTex("= 2")
        self.play(FadeOut(cube, faces[0], edges[0], vertices[0]))
        group = VGroup(faces[1], minus, edges[1], plus, vertices[1])
        solved_group = group.add(number)
        self.play(group.animate.arrange().scale(2))
        self.play(FadeTransformPieces(group, solved_group))
        self.play(Unwrite(solved_group))
        self.play(formula.animate.move_to(ORIGIN).scale(3))
        self.play(Unwrite(formula))
        self.wait(2)
