import os
from castleamongthestars import *
import cloudscraper
from flask import Flask, render_template, request, session, redirect, url_for
from flask_discord import DiscordOAuth2Session
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")

API_BASE_URL = os.environ.get('API_BASE_URL', 'https://discordapp.com/api')
app.config["SECRET_KEY"] = "oogabooga"
base_discord_api_url = 'https://discordapp.com/api'
app.config["DISCORD_CLIENT_ID"] = 123 # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = ""  # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"
discord = DiscordOAuth2Session(app)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


@app.route("/")
def home():
    if not discord.authorized:
        return render_template("main.html")
    return render_template("main.html")


@app.route("/login")
def login():
    if not discord.authorized:
        return discord.create_session(scope=["identify", "guilds", "connections", "guilds.join"])
    return redirect(url_for("user"))


@app.route("/callback")
def callback():
    try:
        discord.callback()
    except Exception:
        pass
    return redirect(url_for("user"))


scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)


@app.route("/mines", methods=['POST'])
def mines_post():
    if not discord.authorized:
        return redirect(url_for("login"))
    userid = discord.fetch_user().id
    dbuser = cluster["users"]
    cursor = dbuser[f"{userid}"]
    check = cursor.find_one({"id": userid})
    usere = discord.fetch_user().name
    hash = (discord.fetch_user()).avatar_hash
    url = f"https://cdn.discordapp.com/avatars/{userid}/{hash}?size=4096"
    if check is None:
        reason = "Denied"
        return render_template("no.html", reason=reason)
    else:
        text = request.form['round']
        roundid = text
        dbround = clustea["round"]
        cursora = dbround[f"{roundid}"]
        checksse = cursora.find_one({"id": roundid})
        if checksse is None:
            token = check['token']
            game = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
            gametrue = game['hasGame']
            if gametrue['hasGame'] == True:
                roundidcheck = game['game']['uuid']
                if roundidcheck == roundid:
                    checks = indpredict()
                    mine1 = checks['mine1']
                    mine2 = checks['mine2']
                    mine3 = checks['mine3']
                    mine4 = checks['mine4']
                    mine5 = checks['mine5']
                    mine6 = checks['mine6']
                    mine7 = checks['mine7']
                    mine8 = checks['mine8']
                    mine9 = checks['mine9']
                    mine10 = checks['mine10']
                    mine11 = checks['mine11']
                    mine12 = checks['mine12']
                    mine13 = checks['mine13']
                    mine14 = checks['mine14']
                    mine15 = checks['mine15']
                    mine16 = checks['mine16']
                    mine17 = checks['mine17']
                    mine18 = checks['mine18']
                    mine19 = checks['mine19']
                    mine20 = checks['mine20']
                    mine21 = checks['mine21']
                    mine22 = checks['mine22']
                    mine23 = checks['mine23']
                    mine24 = checks['mine24']
                    mine25 = checks['mine25']
                    usere = discord.fetch_user().name
                    hash = (discord.fetch_user()).avatar_hash
                    userid = discord.fetch_user().id
                    url = f"https://cdn.discordapp.com/avatars/{userid}/{hash}?size=4096"
                    inserta = {
                        "id": roundid, "mine1": mine1, "mine2": mine2, "mine3": mine3, "mine4": mine4, "mine5": mine5,
                        "mine6": mine6, "mine7": mine7, "mine8": mine8, "mine9": mine9, "mine10": mine10,
                        "mine11": mine11,
                        "mine12": mine12, "mine13": mine13, "mine14": mine14, "mine15": mine15, "mine16": mine16,
                        "mine17": mine17, "mine18": mine18, "mine19": mine19, "mine20": mine20, "mine21": mine21,
                        "mine22": mine22, "mine23": mine23, "mine24": mine24, "mine25": mine25
                    }
                    cursora.insert_one(inserta)
                    addmines = check['mines'] + 1
                    cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
                    return render_template("mines.html", user=usere, pfp=url, mine1=mine1, mine2=mine2, mine3=mine3,
                                           mine4=mine4,
                                           mine5=mine5, mine6=mine6, mine7=mine7, mine8=mine8, mine9=mine9,
                                           mine10=mine10,
                                           mine11=mine11, mine12=mine12, mine13=mine13, mine14=mine14,
                                           mine15=mine15,
                                           mine16=mine16,
                                           mine17=mine17, mine18=mine18, mine19=mine19, mine20=mine20,
                                           mine21=mine21,
                                           mine22=mine22,
                                           mine23=mine23, mine24=mine24, mine25=mine25, roundid=roundid)
                else:
                    reason = "Invalid Round ID"
                    return render_template("no.html", reason=reason)
            else:
                reason = "Unable to predict"
                return render_template("no.html", reason=reason)
        else:
            checks = checksse
            mine1 = checks['mine1']
            mine2 = checks['mine2']
            mine3 = checks['mine3']
            mine4 = checks['mine4']
            mine5 = checks['mine5']
            mine6 = checks['mine6']
            mine7 = checks['mine7']
            mine8 = checks['mine8']
            mine9 = checks['mine9']
            mine10 = checks['mine10']
            mine11 = checks['mine11']
            mine12 = checks['mine12']
            mine13 = checks['mine13']
            mine14 = checks['mine14']
            mine15 = checks['mine15']
            mine16 = checks['mine16']
            mine17 = checks['mine17']
            mine18 = checks['mine18']
            mine19 = checks['mine19']
            mine20 = checks['mine20']
            mine21 = checks['mine21']
            mine22 = checks['mine22']
            mine23 = checks['mine23']
            mine24 = checks['mine24']
            mine25 = checks['mine25']
            addmines = check['mines'] + 1
            cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
            roundids = checks['id']
            return render_template("mines.html", user=usere, pfp=url, mine1=mine1, mine2=mine2, mine3=mine3,
                                   mine4=mine4,
                                   mine5=mine5, mine6=mine6, mine7=mine7, mine8=mine8, mine9=mine9,
                                   mine10=mine10,
                                   mine11=mine11, mine12=mine12, mine13=mine13, mine14=mine14,
                                   mine15=mine15,
                                   mine16=mine16,
                                   mine17=mine17, mine18=mine18, mine19=mine19, mine20=mine20,
                                   mine21=mine21,
                                   mine22=mine22,
                                   mine23=mine23, mine24=mine24, mine25=mine25, roundid=roundids)


@app.route("/mines")
def mines():
    if not discord.authorized:
        return redirect(url_for("login"))
    userid = discord.fetch_user().id
    dbuser = cluster["users"]
    cursor = dbuser[f"{userid}"]
    check = cursor.find_one({"id": userid})
    if check is None:
        reason = "Denied"
        return render_template("no.html", reason=reason)
    else:
        usere = discord.fetch_user().name
        hash = (discord.fetch_user()).avatar_hash
        userid = discord.fetch_user().id
        url = f"https://cdn.discordapp.com/avatars/{userid}/{hash}?size=4096"
        return render_template("mine.html", user=usere, pfp=url)


@app.route("/crash")
def crash():
    if not discord.authorized:
        return redirect(url_for("login"))
    userid = discord.fetch_user().id
    dbuser = cluster["users"]
    cursor = dbuser[f"{userid}"]
    check = cursor.find_one({"id": userid})

    if check is None:
        reason = "Denied"
        return render_template("no.html", reason=reason)

    else:
        usere = discord.fetch_user().name
        hash = (discord.fetch_user()).avatar_hash
        userid = discord.fetch_user().id
        url = f"https://cdn.discordapp.com/avatars/{userid}/{hash}?size=4096"
        geta = crashpredictor()
        addcrash = check['crash'] + 1
        cursor.update_one({"id": userid}, {"$set": {"crash": addcrash}})
        return render_template("crash.html", user=usere, pfp=url, p=geta, a=geta)


@app.route("/user")
def user():
    if not discord.authorized:
        return redirect(url_for("login"))
    userid = discord.fetch_user().id
    dbuser = cluster["users"]
    cursor = dbuser[f"{userid}"]
    check = cursor.find_one({"id": userid})
    hash = (discord.fetch_user()).avatar_hash
    url = f"https://cdn.discordapp.com/avatars/{userid}/{hash}?size=4096"

    if check is None:
        reason = "Denied"
        return render_template("no.html", reason=reason)
    else:
        mines = check['mines']
        crash = check['crash']
        usertoken = check['token']
        user = discord.fetch_user().name
        accoun = account(usertoken)
        subacc = accoun['subacc']
        rank = subacc['rank']
        gamesplay = subacc['gamesPlayed']
        username = subacc['username']
        return render_template("user.html", pfp=url, user=user, m=mines, c=crash, r=rank, g=gamesplay, u=username)


cluster = MongoClient([''])
clustea = MongoClient([''])
if __name__ == "__main__":
    app.run(debug=True)
