
cd client

pyside6-rcc ./view/q_resources.qrc -o q_resources_rc.py
pyside6-uic ./view/ui_form_main.ui > ./view/ui_form_main.py
pyside6-uic ./view/ui_form_com_settings.ui > ./view/ui_form_com_settings.py
pyside6-uic ./view/ui_form_select_variables.ui > ./view/ui_form_select_variables.py
pyside6-uic ./view/ui_form_splash_screen.ui > ./view/ui_form_splash_screen.py
pyside6-uic ./view/ui_form_array_index_table_selected_variables.ui > ./view/ui_form_array_index_table_selected_variables.py
pyside6-uic ./view/ui_form_fra_settings.ui > ./view/ui_form_fra_settings.py
pyside6-uic ./view/ui_form_import_csv.ui > ./view/ui_form_import_csv.py
pyside6-uic ./view/popups/ui_form_popup_scope.ui > ./view/popups/ui_form_popup_scope.py
pyside6-uic ./view/popups/ui_form_popup_scope_cursor.ui > ./view/popups/ui_form_popup_scope_cursor.py
pyside6-uic ./view/popups/ui_form_popup_fra_scope.ui > ./view/popups/ui_form_popup_fra_scope.py
pyside6-uic ./view/popups/ui_form_popup_math_scope.ui > ./view/popups/ui_form_popup_math_scope.py
pyside6-uic ./view/popups/ui_form_popup_table_selected_variables.ui > ./view/popups/ui_form_popup_table_selected_variables.py
pyside6-uic ./view/popups/ui_form_popup_table_variables.ui > ./view/popups/ui_form_popup_table_variables.py
pyside6-uic ./view/popups/ui_form_popup_fft_range.ui > ./view/popups/ui_form_popup_fft_range.py
pyside6-uic ./view/dialogs/ui_form_help.ui > ./view/dialogs/ui_form_help.py

pyside6-lupdate ^
    ./view/ui_form_main.ui ^
    ./view/ui_form_com_settings.ui ^
    ./view/ui_form_select_variables.ui ^
    ./view/ui_form_splash_screen.ui ^
    ./view/ui_form_array_index_table_selected_variables.ui ^
    ./view/ui_form_fra_settings.ui ^
    ./view/ui_form_import_csv.ui ^
    ./view/popups/ui_form_popup_table_variables.ui ^
    ./view/popups/ui_form_popup_scope.ui ^
    ./view/popups/ui_form_popup_scope_cursor.ui ^
    ./view/popups/ui_form_popup_fra_scope.ui ^
    ./view/popups/ui_form_popup_math_scope.ui ^
    ./view/popups/ui_form_popup_table_selected_variables.ui ^
    ./view/popups/ui_form_popup_fft_range.ui ^
    ./view/dialogs/ui_form_help.ui -ts ^
    ./translations/eng-ru.ts

pyside6-lrelease ./translations/eng-ru.ts ./translations/eng-ru.qm

cd ..
