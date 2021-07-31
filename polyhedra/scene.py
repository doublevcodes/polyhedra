from manim import *

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
        self.play(formula.animate.scale(0.3333).to_corner(UL)

        # Create cube and send to corner
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [1, 1, 2],
            [1, -1, 2],
            [-1, 1, 2],
            [-1, -1, 2]
        ]
        faces_list = [
            [0, 1, 2, 3],
            [0, 1, 5, 4],
            [0, 3, 6, 4],
            [2, 1, 5, 7],
            [2, 3, 6, 7],
            [4, 5, 7, 6]
        ]
        cube = Polyhedron(vertex_coords, faces_list).scale(3/2)
        self.play(Create(cube))
        self.play(cube.animate.scale(6/5).to_corner(DL))
