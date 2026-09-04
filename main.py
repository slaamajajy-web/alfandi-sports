from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
import requests

API_KEY = "00cbc61e77644336a40207f569c0d928"
BASE_URL = "https://api.football-data.org/v4/"

class Tab(MDFloatLayout, MDTabsBase):
    pass

class AlFandiSportsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical')
        
        # الهيدر العلوي
        toolbar = MDTopAppBar(
            title="الفندي الرياضية",
            anchor_title="center",
            elevation=4
        )
        layout.add_widget(toolbar)

        # خانة البحث
        search = MDTextField(
            hint_text="ابحث عن بطولة أو فريق...",
            icon_right="magnify",
            size_hint_y=None,
            height="40dp",
            padding=("10dp", "5dp")
        )
        layout.add_widget(search)

        # التبويبات الرئيسية
        tabs = MDTabs()
        tabs.add_widget(Tab(title="الدوريات"))
        tabs.add_widget(Tab(title="الأوروبية"))
        tabs.add_widget(Tab(title="الكؤوس"))
        tabs.add_widget(Tab(title="المحددة"))
        tabs.add_widget(Tab(title="التوقعات"))
        
        layout.add_widget(tabs)
        screen.add_widget(layout)
        return screen

if __name__ == "__main__":
    AlFandiSportsApp().run()
