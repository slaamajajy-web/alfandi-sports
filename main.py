from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
import requests

API_KEY = "00cbc61e77644336a40207f569c0d928"

class Tab(MDFloatLayout, MDTabsBase):
    pass

class AlFandiSportsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical')
        
        toolbar = MDTopAppBar(
            title="الفندي الرياضية",
            anchor_title="center",
            elevation=4
        )
        layout.add_widget(toolbar)

        tabs = MDTabs()
        tabs.add_widget(Tab(title="الدوريات"))
        tabs.add_widget(Tab(title="الكؤوس"))
        tabs.add_widget(Tab(title="المحددة"))
        tabs.add_widget(Tab(title="فرص التوقعات (مطور)"))
        
        layout.add_widget(tabs)
        screen.add_widget(layout)
        return screen

if __name__ == "__main__":
    AlFandiSportsApp().run()
