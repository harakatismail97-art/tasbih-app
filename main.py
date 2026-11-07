import flet as ft

def main(page: ft.Page):
    page.title = "تسبيح"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0F3D2E"

    count = ft.Text("0", size=100, weight=ft.FontWeight.BOLD, color="white")
    dhikr = ft.Text("سبحان الله", size=32, color="#FFD700")
    total = ft.Text("المجموع: 0", size=18, color="white70")

    counter = [0]

    def add(e):
        counter[0] += 1
        count.value = str(counter[0])
        total.value = f"المجموع: {counter[0]}"
        if counter[0] % 33 == 0:
            page.snack_bar = ft.SnackBar(ft.Text("ما شاء الله! كملتي 33"))
            page.snack_bar.open = True
        page.update()

    def reset(e):
        counter[0] = 0
        count.value = "0"
        total.value = "المجموع: 0"
        page.update()

    def change_dhikr(e):
        dhikr.value = e.control.value
        page.update()

    page.add(
        ft.Text("تسبيح", size=40, weight=ft.FontWeight.BOLD, color="#FFD700"),
        dhikr,
        ft.Container(
            content=count,
            width=220, height=220,
            bgcolor="#1A5C42",
            border_radius=110,
            alignment=ft.alignment.center,
            on_click=add,
        ),
        ft.Text("كليكي فالدائرة باش تسبح", color="white70"),
        ft.ElevatedButton("تسبيح +", on_click=add, bgcolor="#FFD700", color="black", width=200, height=50),
        ft.ElevatedButton("تصفير", on_click=reset, bgcolor="white", color="black", width=200),
        ft.Dropdown(
            width=200,
            value="سبحان الله",
            options=[
                ft.dropdown.Option("سبحان الله"),
                ft.dropdown.Option("الحمد لله"),
                ft.dropdown.Option("الله أكبر"),
                ft.dropdown.Option("لا إله إلا الله"),
                ft.dropdown.Option("أستغفر الله"),
            ],
            on_change=change_dhikr,
        ),
        total,
    )

ft.app(target=main)