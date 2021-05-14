screen_helper = """
ScreenManager:
    id: scr_mngr
    HomeScreen:
    NOOScreen:
    SOSScreen:
    FireScreen:
    FirstAidScreen:
    StrangerScreen:
    WeatherScreen:
    PowerOutScreen:
    LockedOutScreen:
    ContactInfoScreen:
    ParentScreen:
    EditFireScreen:
    EditFirstAidScreen:
    EditStrangerScreen:
    EditWeatherScreen:
    EditPowerOutScreen:
    EditLockedOutScreen:
    EditContactInfoScreen:

<HomeScreen>:
    name: "home"
    MDGridLayout:
        cols: 2
        Button:
            #text: "911"
            background_normal: 'resources/911.png'
            on_press: root.manager.current = "noo"
        Button:
            #text: "SOS Text"
            background_normal: 'resources/help.png'
            on_press: root.manager.current = "sos"
        Button:
            #text: "Fire"
            background_normal: 'resources/fire.png'
            on_press: root.manager.current = "fire"
        Button:
            #text: "First Aid"
            background_normal: 'resources/firstaid.png'
            on_press: root.manager.current = "first_aid"
        Button:
            #text: "Stranger Danger"
            background_normal: 'resources/strangerdanger.png'
            on_press: root.manager.current = "stranger"
        Button:
            #text: "Severe Weather"
            background_normal: 'resources/weather.png'
            on_press: root.manager.current = "weather"
        Button:
            #text: "Power Outage"
            background_normal: 'resources/powerout.png'
            on_press: root.manager.current = "power_out"
        Button:
            #text: "Locked Out"
            background_normal: 'resources/lockedout.png'
            on_press: root.manager.current = "locked_out"
        Button:
            text: "Contact Information"
            on_press: root.manager.current = "contact_info"
        Button:
            text: "Parental Control"
            on_press: root.manager.current = "parent"
<NOOScreen>:
    name: "noo"
    MDLabel:
        text: "Calling 911..."
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<SOSScreen>:
    name: "sos"
    MDLabel:
        text: "Calling SOS Contacts..."
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<FireScreen>:
    name: "fire"
    MDLabel:
        id: fire_label
        text: "Fire info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<FirstAidScreen>:
    name: "first_aid"
    MDLabel:
        text: "First aid info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<StrangerScreen>:
    name: "stranger"
    MDLabel:
        text: "Stranger Danger!"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<WeatherScreen>:
    name: "weather"
    MDLabel:
        text: "Severe weather info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<PowerOutScreen>:
    name: "power_out"
    MDLabel:
        text: "Power out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<LockedOutScreen>:
    name: "locked_out"
    MDLabel:
        text: "Locked out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<ContactInfoScreen>:
    name: "contact_info"
    MDLabel:
        text: "Enter contact info here"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"
<ParentScreen>:
    name: "parent"
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Select the category you want to edit"
            font_style: "H5"
            halign: "center"
        ScrollView:
            MDList:
                OneLineIconListItem:
                    text: "Fire"
                    on_release: root.manager.current = "edit_fire"
                OneLineIconListItem:
                    text: "First Aid"
                    on_release: root.manager.current = "edit_first_aid"
                OneLineIconListItem:
                    text: "Stranger Danger"
                    on_release: root.manager.current = "edit_stranger"
                OneLineIconListItem:
                    text: "Severe Weather"
                    on_release: root.manager.current = "edit_weather"
                OneLineIconListItem:
                    text: "Power Outage"
                    on_release: root.manager.current = "edit_power_out"
                OneLineIconListItem:
                    text: "Locked Out"
                    on_release: root.manager.current = "edit_locked_out"
                OneLineIconListItem:
                    text: "Contact Information"
                    on_release: root.manager.current = "edit_contact_info"
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {"center_x":0.5, "center_y":0.9}
        on_press: root.manager.current = "home"

<EditFireScreen>:
    id: edit_fire
    name: "edit_fire"
    MDLabel:
        text: "Enter fire instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        id: fire_input
        multiline: True
        hint_text: "Enter instructions here"
        max_height: "200dp"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: app.get_fire_data()

<EditFirstAidScreen>:
    name: "edit_first_aid"
    MDLabel:
        text: "Enter first aid instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        multiline: True
        hint_text: "Where is the first aid kit? (bandaids, antiseptic, etc.)"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        multiline: True
        hint_text: "Enter other relevant instructions here"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

<EditStrangerScreen>:
    name: "edit_stranger"
    MDLabel:
        text: "Enter stranger danger instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        multiline: True
        hint_text: "List any safety code word(s):"
        helper_text: "a word known by trusted adults only, to prove they can be trusted"
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        multiline: True
        hint_text: "Instructions in case of a break-in"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

<EditWeatherScreen>:
    name: "edit_weather"
    MDLabel:
        text: "Enter severe weather instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        multiline: True
        hint_text: "Enter instructions here"
        helper_text: "weather like hurricanes, tornadoes, tropical storms, etc."
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

<EditPowerOutScreen>:
    name: "edit_power_out"
    MDLabel:
        text: "Power out info (edit)"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

<EditLockedOutScreen>:
    name: "edit_locked_out"
    MDLabel:
        text: "Locked out info (edit)"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

<EditContactInfoScreen>:
    name: "edit_contact_info"
    MDLabel:
        text: "Enter contact info here (edit)"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: root.manager.current = "parent"

"""