from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        """
        只有 Hello World 的首页
        :return:
        """
        return "Hello, world!"

    @app.errorhandler(404)
    def page_not_found():
        """
        以此项目中的404.html作为此Web Server工作时的404错误页
        """
        pass

    @app.route('/pic', methods=['POST'])
    def picture_reshape():
        """
        **请使用 PIL 进行本函数的编写**
        从 b64_url 下载一张图片的 base64 编码，reshape 转为 100*100，并开启抗锯齿（ANTIALIAS）
        对 reshape 后的图片分别使用 base64 与 md5 进行编码，以 JSON 格式返回，参数与返回格式如下
        
        :param: b64_url: 
            本题的 b64_url 以 arguments 的形式给出，可能会出现两种输入
            1. 一个 HTTP URL（Python 类型为 str）
            2. 一个指向TXT 文本文件的 Python 文件对象（Python 类型为 _io.TextIOWrapper）
            该 TXT 文本文件包含一个 HTTP URL
        
        :return: JSON
        {
            "md5": <图片reshape后的md5编码: str>,
            "base64_picture": <图片reshape后的base64编码: str>
        }
        """
        import PIL
        pass

    @app.route('/996')
    def company_996():
        """
        从 github.com/996icu/996.ICU 项目中获取所有的已确认是996的公司名单，并

        :return: 以 JSON List 的格式返回，格式如下
        [{
            "city": <city_name 城市名称>,
            "company": <company_name 公司名称>,
            "exposure_time": <exposure_time 曝光时间>,
            "description": <description 描述>,
            "evidence": <evidence 证据>
        }, ...]
        """
        pass



    return app