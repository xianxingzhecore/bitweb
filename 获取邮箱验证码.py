from bs4 import BeautifulSoup
import mailparser
import re

host ="imap-mail.outlook.com"
# 获取邮箱验证码
def email_code(email, email_pwd,sender):
    from imapclient import IMAPClient

    with IMAPClient(host) as server:
        try:
            server.login(email, email_pwd)
            server.select_folder("INBOX")
            messages = server.search(['UNSEEN', 'FROM',sender])  # in your case: ['FROM', 'email@outlook.example']
            code_list = []
            # messages.reverse()
            for uid, message_data in server.fetch(messages, 'RFC822').items():
                try:
                    email_message = mailparser.parse_from_bytes(message_data[b'RFC822'])
                    soup = BeautifulSoup(email_message.body, "html.parser")
                    msg_body = soup.get_text()

                    s = re.findall(r"\d{6}", str(msg_body).replace("\xa0",''))[0]
                    code_list.append(s)
                except Exception as e:
                    pass

            return code_list[-1]
        except Exception as e:
            return ""





if __name__ == "__main__":
    line = "jwvmdakmwfn@outlook.com----mUuUxW625"
    sender = "mexc"
    line_temp = line.split("----")
    username = line_temp[0]
    password = line_temp[1]


    code = email_code(username, password,sender)
    if code:
        print(f"Code found: {code}")
    else:
        print("No code found in emails.")