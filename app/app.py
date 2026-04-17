@app.route("/reset", methods=["POST"])
def reset():
    r.set("visits", 0)
    return jsonify({"visits": 0})

@app.route("/stats")
def stats():
    visits = r.get("visits") or "0"
    return jsonify({
        "visits": int(visits),
        "hostname": os.uname().nodename
    })
