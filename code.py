from manim import *

class CreateHeartWithText(Scene):
    def construct(self):
        text = "***** is awesome. I like her!!"
        text_display = ""
        for letter in text:
            text_display += letter
            text_mobject = Text(text_display)  
            self.clear()
            self.add(text_mobject)
            self.wait(0.2)
            self.clear()
        heart_curve = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t) ** 3, 
                13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t),  
                0
            ]),
            t_range = np.array([0, TAU]),  
            color=RED,  
            stroke_width=6  
        )
        heart_fill = heart_curve.copy()
        heart_fill.set_fill(RED, opacity=0.5)
        heart_fill.set_stroke(width=0)
        heart_curve.scale(0.2)
        heart_fill.scale(0.2)
        heart_curve.move_to(ORIGIN)
        heart_fill.move_to(ORIGIN)
        self.play(Create(heart_curve), run_time=2)
        self.play(FadeIn(heart_fill), run_time = 2)
