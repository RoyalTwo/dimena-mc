import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    default_font = dpg.add_font("./assets/fonts/segoeui.ttf", 18)

with dpg.window(tag="Primary Window"):
    with dpg.child_window(tag="servers", height=450):
        dpg.add_button(height=150, width=150, label="Add Server")
    with dpg.child_window(tag="control"):
        with dpg.child_window(tag="c_overview", width=300, pos=[0]):
            dpg.add_text(default_value="Server Info")
        with dpg.child_window(tag="c_info", pos=[305]):
            dpg.add_text(default_value="Players Online: 0/20")

    dpg.bind_font(default_font)

dpg.create_viewport(title="Dimena Manager", width=1000, height=700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
