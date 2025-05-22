from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/traj")
def traj():
    letter = request.args.get("letterSel", "Z")
    traj_file = f"{letter}.pdb"
    print(f"Loading trajectory for letter: {letter} -> {traj_file}")
    # You can pass `traj_file` to your template if needed
    return render_template("traj.html", traj_file=traj_file)

if __name__ == "__main__":
    app.run()
