from manim import *

class Title(ThreeDScene):

    def construct(self):

        # Objects needed for the scene
        title_text = Text("Euler's formula for polyhedra")
        formula = MathTex("F", "-", "E", "+", "V", "= 2")
        f_expl = Text("Number of faces").set_color(RED)
        e_expl = Text("Number of edges").set_color(BLUE)
        v_expl = Text("Number of vertices").set_color(YELLOW)
        
        
        # Animation - introduce the formula
        self.play(Write(title_text))
        self.wait(3)
        self.play(Unwrite(title_text))
        self.wait(1)
        self.play(Write(formula))
        self.play(formula.animate.move_to(2.1 * UP), formula.animate.scale(3))
        self.wait(1)

        # Animation - labels for the formula
        for idx, clr, obj, pos in zip((0, 2, 4), (RED, BLUE, YELLOW), (f_expl, e_expl, v_expl), (-2, -1, 0.05)):
            formula[idx].set_color(clr)
            self.play(Write(obj))
            self.play(obj.animate.move_to(pos * UP))

        self.wait(4)
        self.play(FadeOut(f_expl, v_expl, e_expl))
        
        formula_copy = formula.copy().scale(0.3333).to_corner(UL)
        self.play(Transform(formula, formula_copy))
        self.remove(formula)
        formula = formula_copy.copy()
        self.add_fixed_in_frame_mobjects(formula)
        self.remove(formula_copy)

        # Animation - do the cube example to show it works
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        cube = Cube()
        self.play(Create(cube))
        self.wait(3)
        self.play(ApplyMethod(cube.scale, 1.3))
        self.play(ApplyMethod(cube.move_to, 3 * DOWN + 1 * LEFT))
        self.add_fixed_in_frame_mobjects(cube)
        self.wait(2)


        # Animation - cube properties
        faces_label = Text("# of faces = 6").set_color(RED)
        edges_label = Text("# of edges = 12")
        vertices_label = Text("# of vertices = 8")
        self.set_camera_orientation(phi=0, theta=0)
        self.play(Write(faces_label))
        self.play(ApplyMethod(faces_label.shift, 2.5 * UP))
