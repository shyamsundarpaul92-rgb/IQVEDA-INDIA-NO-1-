from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.lang import Builder

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: 0.95, 0.95, 0.98, 1

    MDTopAppBar:
        title: "IQVEDA INDIA NO 1"
        elevation: 4
        pos_hint: {"top": 1}
        md_bg_color: 0.10, 0.20, 0.50, 1

    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            padding: "16dp"
            spacing: "16dp"

            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                adaptive_height: True
                padding: "20dp"
                spacing: "8dp"
                radius: [16,]
                elevation: 4
                md_bg_color: 0.15, 0.28, 0.65, 1

                MDLabel:
                    text: "IQVEDA INDIA NO 1"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    adaptive_height: True

                MDLabel:
                    text: "All in one"
                    halign: "center"
                    font_style: "Subtitle1"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 0.85, 0.2, 1
                    adaptive_height: True

                MDLabel:
                    text: "Robotics, Abacus, Vedic,\\nCompetitive, Computer"
                    halign: "center"
                    font_style: "Body1"
                    theme_text_color: "Custom"
                    text_color: 0.95, 0.95, 0.95, 1
                    adaptive_height: True

                MDLabel:
                    text: "Teacher Training"
                    halign: "center"
                    font_style: "Subtitle2"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 0.8, 1, 0.8, 1
                    adaptive_height: True

            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: "150dp"
                padding: "16dp"
                spacing: "6dp"
                radius: [12,]
                elevation: 3
                md_bg_color: 1, 1, 1, 1

                MDLabel:
                    text: "Class 7-8: Current & Voltage Model"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Primary"

                MDLabel:
                    text: "Water Tank = Battery | Tap = Switch | Pipe = Wire"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Current flows only when potential difference exists."
                    theme_text_color: "Hint"

            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: "140dp"
                padding: "16dp"
                spacing: "6dp"
                radius: [12,]
                elevation: 3
                md_bg_color: 1, 1, 1, 1

                MDLabel:
                    text: "Arduino Uno Core Logic"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Primary"

                MDLabel:
                    text: "void setup() { pinMode(13, OUTPUT); }\\nvoid loop() { digitalWrite(13, HIGH); delay(1000); }"
                    theme_text_color: "Secondary"
'''

class IQvedaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == '__main__':
    IQvedaApp().run()
