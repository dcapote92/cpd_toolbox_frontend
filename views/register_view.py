import flet as ft

def create_register_view(page: ft.Page):
    
    def cancel(e):
        page.snack_bar = ft.SnackBar(ft.Text('Ação Cancelada!'))
        page.go('/login')
        page.open(page.snack_bar)

    def registrate(e):
        page.snack_bar = ft.SnackBar(
            ft.Text('Usuário cadastrado com sucesso!'),
            bgcolor=ft.Colors.GREEN
        )
        page.go('/login')
        page.open(page.snack_bar)


    img_logo = ft.Icon(
        name=ft.Icons.PERSON,
        size=64,

    )

    ctnr_logo = ft. Container(
        content= img_logo,
        alignment=ft.alignment.center
    )

    edt_name = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=36,
        label='Nome',
        enable_suggestions=True,
        autofocus=True,
        capitalization= ft.TextCapitalization.WORDS
    )

    edt_gm_id = ft.TextField(
        multiline=False,
        max_length=9,
        label='Mateus ID',
        enable_suggestions=True,
        hint_text='GM0012345',
        capitalization= ft.TextCapitalization.CHARACTERS
    )
    
    edt_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=15,
        label='Senha',
        password=True,
        can_reveal_password=True
    )
    
    edt_confirm_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=15,
        label='Confirmar senha',
        password=True,
        can_reveal_password=True
    )

    ckb_admin = ft.Checkbox(
        label='Admin',
        value=False
    )

    btn_login = ft.ElevatedButton(
        text='Cadastrar',
        icon= ft.Icons.APP_REGISTRATION_OUTLINED,
        width=120,
        on_click=registrate
    )

    btn_register = ft.ElevatedButton(
        text='Cancelar',
        icon= ft.Icons.CANCEL,
        width=120,
        on_click=cancel
    )

    rw_buttons = ft.Row(
        controls=[
            btn_login,
            btn_register
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    box_container = ft.Container(
        height=800,
        width=400,
        border=ft.border.all(width=3, color=ft.Colors.BLUE_GREY_500),
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ctnr_logo,
                edt_name,
                edt_gm_id,
                edt_password,
                edt_confirm_password,
                ckb_admin,
                rw_buttons
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=30,
    )

 

    return ft.View(
        route='/register',
        controls=[
            box_container,
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
