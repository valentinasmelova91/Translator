import justpy as jp

#@jp.SetRoute('/home')
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

    div1 =jp.Div(a=div, classes='grid grid-cols-2 gap-3 p-4')
    jp.Div(a=div1, text='Hello world', classes ='text-green-500 bg-yellow-500')
    jp.Div(a=div1, text='Hello again')
    in_1 = jp.Input(a=div1, classes='form-input', placeholder='Enter the first value')
    in_2 = jp.Input(a=div1, classes='form-input', placeholder='Enter the second value')
    d_output = jp.Div(a=div1, text='Result goes here...')

    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4')
    jp.Button(a=div2, text='Calculator', click = sum_up, in1=in_1, in2=in_2,
              d = d_output, classes="border border-blue-500 "
                                               "a-2 py-1 px-3 rounded hover:bg-red-500")
    jp.Div(a=div2, text='I am a cool interactive div', classes='hover:bg-red-500',
           mouseenter=mouse_enter, mouseleave=mouse_leave)
    return wp

def sum_up(widget, msg):
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum

def mouse_enter(widget, msg):
   widget.text='A mouse entered'

def mouse_leave(widget, msg):
   widget.text='A mouse left'


#@jp.SetRoute('/about')
#def about():
#    wp = jp.WebPage()
#    jp.Div(a=wp, text='Hello world')
#    jp.Div(a=wp, text='Hello again')
#    return wp

jp.Route("/", home)

jp.justpy(port=9090)