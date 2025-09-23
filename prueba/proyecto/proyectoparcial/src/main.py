import flet as ft

def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    pinturas = [
        {
            "Titulo": "hollow knight",
            "autor": "Team cherry",
            "año": 2017,
            "descripcion": " es un videojuego del género Metroidvania desarrollado por Team Cherry, donde el jugador controla a un pequeño guerrero insectoide sin nombre para explorar el vasto y decaído reino de Hallownest, un lugar plagado por una misteriosa enfermedad",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/imagen%201.jpg",
        },
        {
            "Titulo": "hollow knight",
            "autor": "Team cherry",
            "año": 2017,
            "descripcion": "El protagonizta, inicia su aventura en la ciudad llamada boca sucia",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/imagen2.jpg",
        },
        {
            "Titulo": "hollow knight",
            "autor": "Team cherry",
            "año": 2017,
            "descripcion": "El caballerito explora y llega a la cuidad de lagrima, viendo la estatua y leyendo la historia de hallownest",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/imagen%205.jpg",
        },
        {
            "Titulo": "hollow knight",
            "autor": "Team cherry",
            "año": 2017,
            "descripcion": "El caballerito, llega a enfrentar a el hollow knight, el cual es una vasija que contiene la enfermedad que a matado al reino, y al derrotarlo el caballerito se vuelve la nueva vasija",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/Ending1.jpg",
        },
        {
            "Titulo": "hollow knight",
            "autor": "Team cherry",
            "año": 2017,
            "descripcion": "El caballerito entra en la mente de hollow knight, derrotando a la enfermedad cara a cara llamda, el destello, al derrotarlo las demas almas de las vasijas muertas en batalla, descansaran en paz",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/Ending_3.jpg",
        },
        {
            "Titulo": "Cuphead",
            "autor": "Team MDHR",
            "año": 2017,
            "descripcion": "Cuphead es un videojuego de acción estilo correr y disparar con un enfoque en batallas contra jefes, inspirado en las caricaturas de los años 30. Los jugadores controlan a Cuphead o Mugman en una búsqueda para saldar una deuda con el diablo, recorriendo mundos extraños y adquiriendo nuevas armas. Su principal característica es su estética visual y sonora única, que recrea meticulosamente las técnicas de animación tradicional de la época, utilizando animación a mano, fondos de acuarela y música de jazz original.",
            "imagen":  "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/CupheadRev_Portada.jpg",
        },
        {
            "Titulo": "Cuphead",
            "autor": "Team MDHR",
            "año": 2017,
            "descripcion": "La historia cuenta 2 hermanos que tras ir jugando llegan a el casino del diablo, donde juegan y ganan mucho dinero, pero el diablo dise que apuesten sus almas, si el gana sus almas son de el pero si el pierde les dara riquesa infinita",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/Cuphead-1.jpg.jpg",
        },
        {
            "Titulo": "Cuphead",
            "autor": "Team MDHR",
            "año": 2017,
            "descripcion": "Perdieron los 2 hermanos pero tras rogarle a el diablo, el diablo les dijo que ellos cobraran los contratos de otras personas que quedaron con el diablo, ahora ellos tiene que derrotar a jefes para poder salvar sus vidas.",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/1.2.jpg",
        },
        {
            "Titulo": "Cuphead",
            "autor": "Team MDHR",
            "año": 2017,
            "descripcion": "En el juego hay 2 finales, el final malo trata de que tras recolectar todos los contratos de los deudadores del diablo, decidimos no enfrentar al diablo y darle los contraros nos comenta que si queremos ser parte de el, al decirle que si se lleva las almaas de los hermanosy ahora se vuelven malos.",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/final%201%20cup.jpg",
        },
        {

            "Titulo": "Cuphead",
            "autor": "Team MDHR",
            "año": 2017,
            "descripcion": "El segundo final es que al llegar con el diablo nos dise que si queremos ser parte de el pero al decirle que no empezamos una pelea contra el diablo, y tras derrotarlo, quemamos los contratos con el diablo y salvamos a todos de robarles las almas de los deudadores.",
            "imagen": "https://raw.githubusercontent.com/SNFGK3022/proyecto-parcial3ro/refs/heads/main/final%202%20cup.jpg",
        },
    ]
    
    indice_actual=[0]
    
    contenedor=ft.Container(
        content=ft.Column([]),
        width=550,
        height=650,
        bgcolor=ft.Colors.BLUE_400,
        alignment=ft.alignment.center,
        padding=45
    )
    
    boton_siguiente=ft.ElevatedButton(text="Siguiente Pintura")
    
    def mostrar_pintura():
        pintura=pinturas[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=pintura["imagen"], width=300, height=300, fit=ft.ImageFit.CONTAIN),
            ft.Text(pintura["Titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"autor: {pintura['autor']}",size=16),
            ft.Text(f"año: {pintura['año']}",size=16),
            ft.Text(pintura["descripcion"],size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)

        if indice_actual[0]==len(pinturas)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente pintura"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(pinturas)
        mostrar_pintura()
    boton_siguiente.on_click=siguiente_click

    page.add(
        ft.Container(
            content=ft.Column([
            contenedor,
            boton_siguiente
        ],alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
        ),
        alignment=ft.alignment.center,
        expand=True
        )
    )
    mostrar_pintura()

ft.app(main)