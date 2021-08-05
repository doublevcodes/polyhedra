from manim import *

class Explanation(ThreeDScene):

    def construct(self):
        title = Text("Modifying the formula").shift(3 * UP).scale(1.25)
        self.play(Write(title))
        explanation = MathTex("F", "-",  "E", "+", "V", "=", "2")
        explanation.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation))
        explanation_step2 = MathTex("(F - 1)", "-", "(E - 1)", "+", "V", "=", "2").next_to(explanation, DOWN)
        explanation_step2.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation_step2))
        self.play(VGroup(explanation, explanation_step2).animate.arrange(DOWN))
        explanation_step3 = MathTex("F - 1", "-", "E + 1", "+", "V", "=", "2").next_to(explanation_step2, DOWN)
        explanation_step3.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation_step3))
        self.play(VGroup(explanation, explanation_step2, explanation_step3).animate.arrange(DOWN))
        can_template = TexTemplate()
        can_template.add_to_preamble(r"\usepackage{cancel}")
        explanation_step4 = MathTex(r"F\; \cancel{ -\; 1}", r"-", r"E\; \cancel{ +\; 1}", r"+", r"V", r"=", r"2", tex_template=can_template).next_to(explanation_step3, DOWN)
        explanation_step4.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation_step4))
        self.play(VGroup(explanation, explanation_step2, explanation_step3, explanation_step4).animate.arrange(DOWN))
        expl_sol = explanation.copy().next_to(explanation_step4, DOWN)
        self.play(Write(expl_sol))
        grp = VGroup(explanation, explanation_step2, explanation_step3, explanation_step4, expl_sol)
        line = Line(UP * 2.45, DOWN * 3.5)
        self.play(grp.animate.shift(LEFT * 3.5))
        self.play(Write(line))
        label1 = Text("Remove an edge and face").next_to(explanation, 1.1 * UP).scale(0.75)
        self.play(Write(label1))
        explanation2 = explanation.copy().move_to(RIGHT * 3.5)
        self.play(Write(explanation2))
        explanation2_step2 = MathTex("F", "-", "(E - 1)", "+", "(V - 1)", "=", "2").next_to(explanation2, DOWN)
        explanation2_step2.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation2_step2))
        self.play(VGroup(explanation2, explanation2_step2).animate.arrange(DOWN, center=False).move_to(3.5 * RIGHT))
        explanation2_step3 = MathTex("F", "-", "E + 1", "+", "V - 1", "=", "2").next_to(explanation2_step2, DOWN)
        explanation2_step3.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation2_step3))
        self.play(VGroup(explanation2, explanation2_step2, explanation2_step3).animate.arrange(DOWN, center=False).move_to(3.5 * RIGHT))
        explanation2_step4 = MathTex(r"F", r"-", r"E\; \cancel{ +\; 1}", r"+", r"V\; \cancel{-\;1}", r"=", r"2", tex_template=can_template).next_to(explanation2_step3, DOWN)
        explanation2_step4.set_color_by_tex_to_color_map({
            "F": RED,
            "E": BLUE,
            "V": YELLOW
        })
        self.play(Write(explanation2_step4))
        self.play(VGroup(explanation2, explanation2_step2, explanation2_step3, explanation2_step4).animate.arrange(DOWN, center=False).move_to(3.5 * RIGHT))
        expl2_sol = expl_sol.copy().next_to(explanation2_step4, DOWN)
        self.play(Write(expl2_sol))
        label2 = Text("Remove an edge and vertex").next_to(explanation2, 1.1 * UP).scale(0.75)
        self.play(Write(label2))
        self.play(*[Unwrite(mobject) for mobject in self.mobjects])
        self.wait()