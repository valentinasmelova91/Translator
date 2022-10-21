import justpy as jp
from webApp import layout, page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="This is the About page!", classes='text-4xl m-2')
        jp.Div(a=div, text="""
        This application has a functionality of instant translation from English to English. 
        In case you do not know the meaning of some English words - feels free to try it out!
        """, classes="text-lg")
        return wp
