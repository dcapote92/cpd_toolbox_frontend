import flet as ft
import re

def create_register_view(page: ft.Page):
    
    # controls reference
    edt_name = None
    edt_gm_id = None
    edt_password = None
    edt_confirm_password = None
    btn_registrate = None

    # validation functions

    def check_all_valid():
        is_name_valid = bool(edt_name.value) and not edt_name.error_text
        is_id_valid = bool(edt_gm_id.value) and not edt_gm_id.error_text
        is_pass_valid = bool(edt_password.value) and not edt_password.error_text
        is_confirm_valid = bool(edt_confirm_password) and not edt_confirm_password.error_text

        btn_registrate.disabled = not (is_name_valid and is_id_valid and is_pass_valid and is_confirm_valid)
        btn_registrate.update()

    def validate_name(e):
        name = e.control.value
        if not name or len(name) < 3:
            e.control.error_text = 'Nome deve ter no mínimo 3 caracteres.'
        else: e.control.error_text = None

        e.control.update()
        check_all_valid()

    def validate_gm_id(e):
        gm_id = e.control.value
        if not re.fullmatch(r'GM\d{7}', gm_id.upper()):
            e.control.error_text = 'Mateus ID inválido. Formato esperado GM1234567.' 
        else: e.control.error_text = None

        e.control.update()
        check_all_valid()

    def validate_password(e):
        password = e.control.value

        if len(password) < 8:
            e.control.error_text = 'A senha deve ter no mínimo 8 caracteres.'
        elif not re.search(r'[0-9]', password):
            e.control.error_text = 'A senha deve ter pelo menos um número'
        elif not re.search(r'[a-z]', password):
            e.control.error_text = 'A senha deve ter pelo menos uma letra minúscula.'
        elif not re.search(r'[A-Z]', password):
            e.control.error_text = 'A senha deve ter pelo menos uma letra maiúscula.'
        elif not re.search(r'[!@#$%^&*()_+=\[{\]};:\'\"\\|,.<>\/?~-]', password):
            e.control.error_text = 'A senha deve ter pelo menos um caractere especial.'
        else: e.control.error_text = None
        
        e.control.update()
        validate_confirm_password(None)
        check_all_valid()

    def validate_confirm_password(e):
        confirm_password = edt_confirm_password.value
        password = edt_password.value

        if not confirm_password:
            edt_confirm_password.error_text = 'Confirmação de senha é obrigatória.'
        elif password != confirm_password:
            edt_confirm_password.error_text = 'As senhas não coincidem.'
        else: edt_confirm_password.error_text = None

        edt_confirm_password.border_color= ft.Colors.GREEN_700 if password == confirm_password else None

        edt_confirm_password.update()
        check_all_valid()
        
    # action functions        

    def cancel(e):
        page.snack_bar = ft.SnackBar(
            ft.Text('Ação Cancelada!'),
            bgcolor=ft.Colors.YELLOW_700
        )
        page.go('/login')
        page.open(page.snack_bar)
        page.update()

    def registrate(e):
        page.snack_bar = ft.SnackBar(
            ft.Text('Usuário cadastrado com sucesso!'),
            bgcolor=ft.Colors.GREEN_700
        )
        page.go('/login')
        page.open(page.snack_bar)
        page.update()

    # ui controls

    img_logo = ft.Icon(
        name=ft.Icons.PERSON_ADD_ALT_1,
        size=64,
        color=ft.Colors.BLUE_700
    )

    ctnr_logo = ft. Container(
        content= img_logo,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=10, bottom=30)
    )

    edt_name = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=36,
        label='Nome Completo',
        enable_suggestions=True,
        autofocus=True,
        capitalization= ft.TextCapitalization.WORDS,
        on_change=validate_name
    )

    edt_gm_id = ft.TextField(
        multiline=False,
        max_length=9,
        label='Mateus ID',
        enable_suggestions=True,
        hint_text='GM1234567',
        capitalization= ft.TextCapitalization.CHARACTERS,
        on_change=validate_gm_id
    )
    
    edt_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=20,
        label='Senha',
        password=True,
        can_reveal_password=True,
        on_change=validate_password,
        helper_text='Minimo 8 caracteres, letras Maiúsculas, Minúsculas, Número e Símbolo.'
    )
    
    edt_confirm_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=20,
        label='Confirmar senha',
        password=True,
        can_reveal_password=True,
        on_change=validate_confirm_password
    )

    ckb_admin = ft.Checkbox(
        label='Admin',
        value=False,
        tooltip='Designar este usuário como administrador'
    )

    btn_registrate = ft.ElevatedButton(
        text='Cadastrar',
        icon= ft.Icons.APP_REGISTRATION_OUTLINED,
        width=120,
        on_click=registrate,
        bgcolor=ft.Colors.GREEN_700,
        color=ft.Colors.WHITE,
        disabled=True
    )

    btn_cancel = ft.ElevatedButton(
        text='Cancelar',
        icon= ft.Icons.CANCEL,
        width=120,
        on_click=cancel
    )

    rw_buttons = ft.Row(
        controls=[
            btn_registrate,
            btn_cancel
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    box_container = ft.Container(
        height=800,
        width=400,
        border=ft.border.all(width=3, color=ft.Colors.BLUE_GREY_300),
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
                ft.Divider(height=20,color=ft.Colors.TRANSPARENT),
                rw_buttons
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=30,
    )

    # this is necessary for functions that have late execution can access them
    globals().update(
        edt_name=edt_name,
        edt_gm_id=edt_gm_id,
        edt_password=edt_password,
        edt_confirm_password=edt_confirm_password,
        btn_registrate=btn_registrate
    )

    return ft.View(
        route='/register',
        controls=[
            box_container,
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
