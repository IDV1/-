import ollama as ol
import socket as so

def response_chat(content, role="user", model_case="qwen3:0.6b"):
    response = ol.chat(
        model=model_case,
        messages=[{"role": role, "content": content}]
    )
    print(response["message"]["content"])

def get_localhostip():
    # 自动获取本机IP地址
    hostname = so.gethostname()
    local_ip = so.gethostbyname(hostname)
    ollama_url = f"http://{local_ip}:11434"
    localhost = ol.Client(host=ollama_url)
    print(f"Ollama 本地地址: {ollama_url}")
    print(localhost)

def list_models():
    models_info = ol.list()
    print("现在已安装的模型:")
    for m in models_info["models"]:
        print(f"模型名称: {m['name']}")

def show_model_info(model_name):
    print(ol.show(model_name))

def list_running_models():
    print("正在运行的模型:")
    print(ol.ps())

def change_model():
    list_models()
    scan03 = input("请输入更改的模型名称>>>")
    if scan03.strip() != "":
        print(f"已切换到模型: {scan03}")
        return scan03
    else:
        print("错误,请重试!")
        return None

def set_role():
    role = input("请输入角色（如user、system等）>>>")
    if role.strip() != "":
        print(f"角色已设定为: {role}")
        return role
    else:
        print("角色输入有误，使用默认user")
        return "user"

print("====与ChatGPT聊天====")
print("")
print("1.聊天")
print("2.设定角色")
print("3.列出安装的模型")
print("4.显示固定模型信息")
print("5.列出正在运行的模型")
print("6.修改模型")
print("7.获取本地客户端ip地址")
print(" ")
print("====================")

current_model = "qwen3:0.6b"
current_role = "user"

while True:
    scan01 = input("请输入功能编号(1-6，q退出)...")
    if scan01 == "1":
        scan02 = input("请输入聊天内容>>>")
        if scan02.strip() == "1":
            print("退出成功!")
            break
        elif scan02.strip() != "":
            response_chat(content=scan02, role=current_role, model_case=current_model)
        else:
            print("请再输入一遍")
    elif scan01 == "2":
        current_role = set_role()
    elif scan01 == "3":
        list_models()
    elif scan01 == "4":
        show_model_info(current_model)
    elif scan01 == "5":
        list_running_models()
    elif scan01 == "6":
        new_model = change_model()
    elif scan01 == "7":
        get_localhostip()
        if new_model:
            current_model = new_model
    elif scan01.lower() == "q" or scan01.upper() == "Q":
        print("程序已退出。")
        break
    else:
        print("无效输入，请重新选择。")

