screen_helper = """
# Add each Screen to the ScreenManager
ScreenManager:
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

# Create the home screen with a button for each emergency that goes to the corresponding Screen
<HomeScreen>:
    name: "home"
    MDGridLayout:
        cols: 2
        # Button:
        #     #text: "911"
        #     background_normal: 'resources/911.png'
        #     on_press: root.manager.current = "noo"
        # Button:
        #     #text: "SOS Text"
        #     background_normal: 'resources/help.png'
        #     on_press: root.manager.current = "sos"
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

# <NOOScreen>:
#     name: "noo"
#     MDLabel:
#         text: "Calling 911..."
#         halign: "center"
#     MDRectangleFlatButton:
#         text: "Back"
#         pos_hint: {"center_x":0.5, "center_y":0.2}
#         on_press: root.manager.current = "home"

# <SOSScreen>:
#     name: "sos"
#     MDLabel:
#         text: "Calling SOS Contacts..."
#         halign: "center"
#     MDRectangleFlatButton:
#         text: "Back"
#         pos_hint: {"center_x":0.5, "center_y":0.2}
#         on_press: root.manager.current = "home"

# Define the fire Screen to display the given input
<FireScreen>:
    name: "fire"
    MDLabel:
        id: fire_label
#        text: "Fire info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the first aid Screen to display the given input
<FirstAidScreen>:
    name: "first_aid"
    MDLabel:
        id: first_aid_label
#        text: "First aid info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the stranger danger Screen to display the given input
<StrangerScreen>:
    name: "stranger"
    MDLabel:
        id: stranger_label
#        text: "Stranger Danger!"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the severe weather Screen to display the given input
<WeatherScreen>:
    name: "weather"
    MDLabel:
        id: weather_label
#        text: "Severe weather info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the power outage Screen to display the given input
<PowerOutScreen>:
    name: "power_out"
    MDLabel:
        id: power_out_label
#        text: "Power out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the locked out Screen to display the given input
<LockedOutScreen>:
    name: "locked_out"
    MDLabel:
        id: locked_out_label
#        text: "Locked out info"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the contact information Screen to display the given input
<ContactInfoScreen>:
    name: "contact_info"
    MDLabel:
        text: "Enter contact info here"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "home"

# Define the parent Screen with a menu of emergencies for the parent to chose from
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
                # OneLineIconListItem:
                #     text: "Contact Information"
                #     on_release: root.manager.current = "edit_contact_info"
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {"center_x":0.5, "center_y":0.9}
        on_press: root.manager.current = "home"

# Define the edit fire Screen to get the input from the user
<EditFireScreen>:
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
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[3].ids.fire_label.text = "Fire Instructions: \\n" 
            root.manager.screens[3].ids.fire_label.text += root.ids.fire_input.text
            root.manager.current = 'parent'

# Define the edit first aid Screen to get the input from the user
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
        id: first_aid_input1
        multiline: True
        hint_text: "Where is the first aid kit? (bandaids, antiseptic, etc.)"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        id: first_aid_input2
        multiline: True
        hint_text: "Enter other relevant instructions here"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[4].ids.first_aid_label.text = "Where to find first aid things: \\n"
            root.manager.screens[4].ids.first_aid_label.text += root.ids.first_aid_input1.text
            root.manager.screens[4].ids.first_aid_label.text += "\\n\\n First Aid Instructions: \\n"
            root.manager.screens[4].ids.first_aid_label.text += root.ids.first_aid_input2.text
            root.manager.current = "parent"

# Define the edit stranger danger Screen to get the input from the user
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
        id: stranger_input1
        multiline: True
        hint_text: "List any safety code word(s):"
        helper_text: "a word known by trusted adults only, to prove they can be trusted"
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        id: stranger_input2
        multiline: True
        hint_text: "Instructions in case of a break-in"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[5].ids.stranger_label.text = "Safety code words: \\n"
            root.manager.screens[5].ids.stranger_label.text += root.ids.stranger_input1.text
            root.manager.screens[5].ids.stranger_label.text += "\\n\\n Break-in Instructions: \\n"
            root.manager.screens[5].ids.stranger_label.text += root.ids.stranger_input2.text
            root.manager.current = "parent"

# Define the edit severe weather Screen to get the input from the user
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
        id: weather_input
        multiline: True
        hint_text: "Enter instructions here"
        helper_text: "weather like hurricanes, tornadoes, tropical storms, etc."
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDRectangleFlatButton:
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[6].ids.weather_label.text = "Severe Weather Instructions: \\n" 
            root.manager.screens[6].ids.weather_label.text += root.ids.weather_input.text
            root.manager.current = 'parent'

# Define the edit power outage Screen to get the input from the user
<EditPowerOutScreen>:
    name: "edit_power_out"
    MDLabel:
        text: "Enter power outage instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        id: power_out_input1
        multiline: True
        hint_text: "Where are the flashlights?"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        id: power_out_input2
        multiline: True
        hint_text: "Other relevant information:"
        helper_text: "i.e. where to find candles, about a generator etc."
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[7].ids.power_out_label.text = "Where to find flashlights: \\n"
            root.manager.screens[7].ids.power_out_label.text += root.ids.power_out_input1.text
            root.manager.screens[7].ids.power_out_label.text += "\\n\\n Power out Instructions: \\n"
            root.manager.screens[7].ids.power_out_label.text += root.ids.power_out_input2.text
            root.manager.current = "parent"

# Define the edit locked out Screen to get the input from the user
<EditLockedOutScreen>:
    name: "edit_locked_out"
    MDLabel:
        text: "Enter power outage instructions"
        font_style: "H6"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.8}
    MDLabel:
        text: "Be sure that your instructions can be understood by your child"
        font_style: "Caption"
        halign: "center"
        pos_hint: {"center_x":0.5,"center_y":0.7}
    MDTextField:
        id: locked_out_input1
        multiline: True
        hint_text: "Where is the spare key?"
        pos_hint: {"center_x":0.5,"center_y":0.5}
    MDTextField:
        id: locked_out_input2
        multiline: True
        hint_text: "Other relevant information:"
        helper_text: "i.e. who to call, where to go, etc."
        helper_text_mode: "persistent"
        pos_hint: {"center_x":0.5,"center_y":0.3}
    MDRectangleFlatButton:
        text: "Save & Exit"
        pos_hint: {"center_x":0.5, "center_y":0.1}
        on_press: 
            root.manager.screens[8].ids.locked_out_label.text = "Where to find spare key: \\n"
            root.manager.screens[8].ids.locked_out_label.text += root.ids.locked_out_input1.text
            root.manager.screens[8].ids.locked_out_label.text += "\\n\\n Locked out Instructions: \\n"
            root.manager.screens[8].ids.locked_out_label.text += root.ids.locked_out_input2.text
            root.manager.current = "parent"

# <EditContactInfoScreen>:
#     name: "edit_contact_info"
#     MDLabel:
#         text: "Enter contact info here (edit)"
#         halign: "center"
#     MDRectangleFlatButton:
#         text: "Back"
#         pos_hint: {"center_x":0.5, "center_y":0.1}
#         on_press: root.manager.current = "parent"

"""
