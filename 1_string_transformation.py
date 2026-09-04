booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "


record = booking.strip()

parts = record.split(' | ')

event_code = parts[0]                 
name = parts[1].title()               
room = parts[2].upper()               
time = parts[3]                       
email = parts[4]                      
vip_tag = parts[5]                    

at_pos = email.find('@')
email_domain = email[at_pos + 1:].lower() 

vip_count = vip_tag.count('VIP')


valid_event = event_code.startswith('EVT') and '-' in event_code


valid_user = '_' in parts[1] 

valid_room = 'ROOM' in room

valid_time = ':' in time

valid_email = '@' in email and '.' in email

print(f"""Event code: {event_code}
Name: {name}
Room: {room}
Time: {time}
Email domain: {email_domain}
VIP tag count: {vip_count}
Valid event code: {valid_event}
Valid username: {valid_user}
Valid room: {valid_room}
Valid time: {valid_time}
Valid email: {valid_email}""")

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """
