import flask
import qrcode
app = flask.Flask(__name__)

@app.route("/")
def home():
    # data = flask.request.args.get("data")
    # #第二部，生成二维码
    # img = qrcode.make(data)
    # img.save(r"C:\Users\Administrator\Desktop\day6\qrcode_tool_online\static/qr.png")
    
    # #第三步，在页面上显示二维码图片sas
    # return '<img src="/static/qr.png"/>'
    return flask.render_template('qr_tool.html')

@app.route("/qr",methods=["POST"])
def qr():
    data = flask.request.form.get("data")
    print
        # #第二部，生成二维码
    img = qrcode.make(data)
    img.save(r"C:\Users\Administrator\Desktop\day6\qrcode_tool_online\static/qr.png")
    
    # #第三步，在页面上显示二维码图片
    return '<img src="/static/qr.png"/>'






if __name__ == '__main__':
    app.run(debug=True)