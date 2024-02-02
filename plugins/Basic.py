from hydrogram import Client, filters
from hydrogram.enums import ChatAction
from lib.env import config_tool

@Client.on_message(filters.command("helps"))
def help_list(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    m.reply(f"""Xin chào **{m.from_user.first_name}**(`{m.from_user.id}`), dưới đây là danh sách lệnh khả dụng:
    
/get - Lấy liên kết tổng hợp subscribe

/add - Thêm subscribe 

/checkv2ray - Kiểm tra subscription

/share - Chia sẻ subscribe 

/test - Kiểm tra cấu hình v2ray...

/mylist - Danh sách subscribe của tôi

/remove - Xoá subscribe khỏi danh sách

/checkall - Tự kiểm tra và xoá subscribe bị lỗi (không bao gồm subscribe hết lưu lượng truy cập)

/request [get, post, put, delete, option] - Gửi yêu cầu HTTP

/sharelist - Lấy danh sách note chung

/rmshare - Xoá subscribe khỏi note chung 

/checkshare - Kiểm tra và xoá khỏi note chung

/ext - Nâng cao
""", quote=True)

@Client.on_message(filters.command("ext"))
def ext_command_list(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    m.reply(f"""**{m.from_user.first_name}**(`{m.from_user.id}`), lệnh nâng cao:

/testall - Sử dụng tất cả địa điểm test
    	
/addpoint - `None`

/testservers - Lấy danh sách địa điểm test

/delpoint - None

/install - Hướng dẫn thiết lập địa điểm test

/addserver - Thêm máy chủ SHH

/delserver - Xoá máy chủ SSH 

/machines - Danh sách máy chủ SSH đã thêm 

.`tên máy` - Chạy lệnh shell trên máy chủ SSH
""", quote=True
)

@Client.on_message(filters.command("install"))
def help_install_endpoint(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    m.reply("**Thiết lập với Docker:**\n`docker run -e PREFIX=(nhập prefix vào đây) -e NAME=(nhập tên vào đây) -d ghcr.io/bosuutap/writer-endpoint:main`\n\n**Thiết lập thủ công:**\n`git clone https://github.com/bosuutap/writer-endpoint && cd writer-endpoint && pip install -r requirements.txt && bash setup.sh`\n\n**Sau đó chạy bằng lệnh:** `python start.py (nhập prefix vào đây) (tên của bạn vào đây)`", quote=True)

@Client.on_message(filters.command(["start","help"]))
def send_welcome(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    m.reply_text(f"Xin chào {m.from_user.first_name}(`{m.from_user.id}`)\nDùng lệnh /helps để biết thêm chi tiết", quote=True)