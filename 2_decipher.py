encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""
chunks = encoded.split('|')

fragments = []

for chunk in chunks:
    if '[' in chunk and ']' in chunk:
        start = chunk.find('[') + 1
        end = chunk.find(']')
        content = chunk[start:end]
        fragments.append(content)

messages = {}

for item in fragments:
    parts = item.split('::')
    if len(parts) == 3:
        num_str = parts[0]
        text = parts[1]
        status = parts[2]
        
        if status == 'ok':
            num = int(num_str)
            
            decoded_text = ""
            for char in text:
                if char == '_' or char.isdigit():
                    decoded_text += char
                else:
                    new_char_code = ord(char) - num
                    decoded_text += chr(new_char_code)
         
            messages[num] = decoded_text


final_message_list = []
for key in sorted(messages):
    final_message_list.append(messages[key])

final_message = " ".join(final_message_list)

print(final_message)
###############################################################
"""
1. Part of the real message is inside the the '[' and ']' brackets.
2. Each fragment inside the brackets has a number, jumbled text of the message, and 'ok'. Focus on only those fragments. The '::' are just separating these parts in the fragment 
3. To find the actual message in every fragment,take every letter in the jumbled message, and shift it backward by the number part in that fragment
For example, if the number is 3 and the jumbled message is ABC, then the actual message is XYZ.
Similarly, if the number is 5 and the jumbled message is ABC, then the actual message is VWX.
4. Ignore any fragment that has 'bad' instead of 'ok'.
5. Once you have decoded all the fragments, combine them in the order of their numbers to get the final message. First comes the fragment with number 1, then 2, and so on.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


