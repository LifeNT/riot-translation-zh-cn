# -*- coding: utf-8 -*-

#说明：这个脚本程序可以读取riot的界面字符串，替换为中文字符
#最新版本riot下载地址：https://github.com/vector-im/riot-web
 
import re,os,sys


#重命名源文件，作为备份

sourcefile = raw_input("Please input your bundle.*.js file full name:")

if not os.path.isfile( sourcefile ):
     print "File does not exists！"
     sys.exit(0)
else:
          bak = sourcefile+".bak"
          if os.path.isfile( bak ) :             
             print "the '"+bak+"'file already exist, please rename it manully"
          else:
             os.rename ( sourcefile , bak )
      



#字符串替换函数，按照 word_dic 定义的词汇表进行替换
def replace_words(text, word_dic):
    rc = re.compile('|'.join(map(re.escape, word_dic)))
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)
 
 
# 读取原js文件

fin = open(bak, "r")
en_strings = fin.read()
fin.close()

 
# 字义需要替换的字符串

word_dic = {
'null,"Sign in",a':'null,"登录",a',
'placeholder:"Email or user name"':'placeholder:"用户名或Email地址"',
'placeholder:"Password"':'placeholder:"密码"',
'"Forgot your password?")':'"忘记密码？")',
'"Default server")':'"默认服务器")',
',"Custom server")':',"自定义服务器")',
'value:"Sign in"':'value:"登录"',
'"Create a new account"':'"注册新帐号"',
'"Login as guest"':'"以访客(guest)身份登录"',
'"Return to app"':'"返回聊天界面"',
'"Home server URL"':'"节点服务器地址"',
'"Identity server URL"':'"身份验证服务器地址"',
'"What does this mean?"':'"查看说明"',
'"Custom Server Options"':'"自定义服务器-注意事项"',
'"You can use the custom server options to sign into other Matrix servers by specifying a different Home server URL."':'"填写自定义节点服务器地址，就可以登录到你指定的matrix服务器"',
'"This allows you to use Riot with an existing Matrix account on a different home server."':'"这将允许你使用其它matrix服务器的帐号，通过Riot客户端进行登录"',
'"You can also set a custom identity server but you won\'t be able to invite users by email address, or be invited by email address yourself."':'"你也可以使用自定义的身份验证服务器，那样你将无法通过Email地址邀请他人"',
'"Dismiss"':'"取消"',
'"To reset your password, enter the email address linked to your account:"':'"请输入你绑定的邮箱地址来找回密码"',
'placeholder:"Email address"':'placeholder:"邮箱地址"',
'placeholder:"New password"':'placeholder:"新密码"',
'placeholder:"Confirm your new password"':'placeholder:"再次输入你的新密码"',
'value:"Send Reset Email"':'value:"发送重置密码的邮箱"',
'"The email address linked to your account must be entered."':'"邮箱地址不能为空！"',
'"OK"':'"确定"',
'title:"Error"':'title:"错误"',
'"Return to login"':'"返回登录"',
'label:"Favourites"':'label:"收藏"',
'label:"Favourite"':'label:"收藏"',
'label:"People"':'label:"私聊"',
'label:"Rooms"':'label:"群聊"',
'label:"Low priority"':'label:"不常用"',
'label:"Historical"':'label:"已退出的聊天室"',
'"You are not receiving desktop notifications. "':'"你尚未启用桌面消息提醒，"',
'"Enable them now"':'"立即启用"',
'label:"Drop here to "':'label:"拖放到此新增 "',
'verb:"favourite"':'verb:"收藏"',
'verb:"restore"':'verb:"群聊"',
'verb:"demote"':'verb:"不常用"',
'"Logout"':'"登出"',
'"Filter room names"':'"搜索聊天室（名称）"',
'"You are Rioting as a guest. "':'"当前正以访客身份登录 请"',
'r.createElement("a",{onClick:this.onRegisterClicked},"Register")':'r.createElement("a",{onClick:this.onRegisterClicked},"注册")',
'" to access more rooms and features."':'" 以使用全部功能！"',
'"sign in"':'"登录"',
'"Create an account"':'"注册新用户"',
'placeholder:"Email address (optional)"':'placeholder:"邮箱地址（可选）"',
'"Missing password."':'"密码不得为空"',
'"Passwords don\'t match."':'"两次输入的密码不一致"',
'"Password too short (min "+d+")."':'"密码太短 (至少 "+d+"位)."',
'"This doesn\'t look like a valid email address"':'"Email地址不合法"',
'"User names may only contain letters, numbers, dots, hyphens and underscores."':'"用户名只能包含字母、数字、英文句号（.），英文连字符（-），英文下划线（_）"',
'"You need to enter a user name"':'"用户名不得为空"',
'"An unknown error occurred."':'"发生未知错误"',
'var r="User name"':'var r="用户名"',
'placeholder:"Confirm password"':'placeholder:"确认密码"',
'"Guest users can\'t invite users. Please register to invite."':'"访客不能邀请他人，请注册。"',
'"Register"':'"注册"',
'"I already have an account"':'"我已经拥有一个帐号"',
'"Start a new chat"':'"开始新的私聊"',
'"Who would you like to communicate with?"':'"请输入对方帐号信息"',
'placeholder:"User ID, Name or email"':'placeholder:"用户ID，昵称，Email地址"',
'"Start Chat"':'"开始聊天"',
'title:"Directory"':'title:"聊天室列表"',
'"Create Room"':'"创建聊天室"',
'"Room name (optional)"':'"请输入聊天室名称（可选）"',
'"Cancel"':'"取消"',
'getLabel("Start chat"':'getLabel("开始私聊"',
'getLabel("Room directory"':'getLabel("聊天室列表"',
'getLabel("Create new room"':'getLabel("新建聊天室"',
'getLabel("Settings"':'getLabel("设置"',
'"A new password must be entered."':'"密码不得为空！"',
'"Setting a user name will create a fresh account"':'"输入新用户名将创建一个全新的用户"',
'title:"Settings"':'title:"设置"',
'createElement("h3",null,"Profile"':'createElement("h3",null,"个人资料"',
'"Display name"':'"昵称"',
'createElement("h3",null,"Account"':'createElement("h3",null,"账号管理"',
'"Sign out"':'"退出登录"',
'createElement("h3",null,"User Interface"':'createElement("h3",null,"用户界面设置"',
'"Disable inline URL previews by default"':'"禁用聊天室内超链接（URL）预览"',
'createElement("h3",null,"Labs"':'createElement("h3",null,"实验功能"',
'"These are experimental features that may break in unexpected ways. Use with caution."':'"以下功能属于实验性质，可能引发程序错误，请谨慎使用"',
'"Guests can\'t use labs features. Please register."':'"访客不能使用实验功能，请注册为正式用户"',
'"Please Register"':'"请注册为正式用户"',
'"Rich Text Editor"':'"高级文本编辑器"',
'"Devices"':'"登录过的设备"',
'"Cryptography"':'"密钥信息"',
'"device id':'"设备ID',
'"Device ID':'"设备ID',
'"Device key:"':'"设备密钥:"',
'createElement("h3",null,"Advanced"':'createElement("h3",null,"详细登录信息"',
'"Logged in as "':'"当前登录ID：    "',
'"Homeserver is "':'"当前登录节点：   "',
'"Identity Server is "':'"身份验证服务器： "',
'"matrix-react-sdk version: "':'"matrix-react-sdk 版本号： "',
'"vector-web version: "':'"vector-web 版本号： "',
'"olm version: "':'"olm 版本号： "',
'"Last seen"':'"最后登录"',
'deviceName"},"Name"':'deviceName"},"设备名称"',
'deviceId"},"ID"':'deviceId"},"登录ID"',
'"Guests can\'t set avatars. Please register."':'"访客不能设置头像，请注册成为正式用户！"',
'"No rooms to show"':'当前位置没有任何聊天室',
'placeholder:"Add email address"':'placeholder:"添加Email（输完后点右侧+号）"',
'"Current password"':'"当前密码"',
'"New password"':'"新密码"',
'"Confirm password"':'"再次输入新密码"',
'"Passwords can\'t be empty"':'"密码不能为空"',
'"New passwords don\'t match."':'"两次输入的密码不一致"',
'"Change Password"':'"修改密码"',
'"h3",null,"Notifications"':'"h3",null,"通知设置"',
'"Enable notifications for this account"':'"开启当前帐号的通知功能"',
'"Enable desktop notifications"':'"启用桌面电脑消息通知"',
'"Enable audible notifications in web client"':'"在web客户端中启用新消息提示音"',
'"Add an email address above to configure email notifications"':'"注意：添加Email地址后，可以启用邮件通知"',
'"Messages containing my name"':'"新消息中提到我的名字"',
'"Messages containing "':'"新消息中含有指定"',
'onKeywordsClicked},"keywords"':'onKeywordsClicked},"关键字"',
'"Enter keywords separated by a comma:"':'"请输入关键字，可使用英文逗号分隔多个关键字"',
'"Messages in one-to-one chats"':'"新的私聊消息"',
'"Messages in group chats"':'"新的群聊消息"',
'"When I\'m invited to a room"':'"收到邀请加入新的聊天室"',
'"Call invitation"':'"收到语音聊天邀请"',
'"Messages sent by bot"':'"收到机器人发来的消息"',
'"Notification targets"':'"接收通知的设备"',
'"Deactivate Account"':'"销毁帐号"',
'"Deactivate my account"':'"确认销毁帐号"',
'"Tagged as: "':'"将该聊天室标注为："',
'"Who can access this room?"':'"谁能进入该聊天室？"',
'"Only people who have been invited"':'"仅允许受邀请的人"',
'"Anyone who knows the room\'s link, apart from guests"':'"除访客以外的所有人"',
'"Anyone who knows the room\'s link, including guests"':'"任何人，包括访客"',
'"Enable encryption (warning: cannot be disabled again!)"':'"开启加密（开启后不能关闭！）"',
'"List this room in "':'"将该聊天室加入节点服务器 "',
'"\'s room directory?"':' " 的公开列表"',
'"Who can read history?"':'"谁能查看历史聊天记录？"',
'"Privacy warning"':'"隐私警告"',
'"Changes to who can read history will only apply to future messages in this room."':'"修改此处仅会影响改变设置后的新聊天记录"',
'"The visibility of existing history will be unchanged."':'"已经有权查看的聊天记录不受设置变更的影响！"',
'onComplete},"Continue"':'onComplete},"确认"',
'button:"Continue"':'button:"确认"',
'"Members only (since the point in time of selecting this option)"':'"仅成员可见（从选中此项开始）"',
'"Anyone"':'"任何人"',
'"Members only (since they were invited)"':'"仅成员可见（从他们收到邀请开始）"',
'"Members only (since they joined)"':'"仅成员可见（从他们加入聊天室开始）"',
'"Room Colour"':'"聊天室配色"',
'"addresses"':'"聊天室地址"',
'"The main address for this room is: "':'"本聊天室的主地址："',
'"This room has no local addresses"':'"本聊天室还没有本地节点地址"',
'placeholder:"New address (e.g.':'placeholder:"添加地址(例如 ',
'"Remote addresses for this room:"':'"本聊天室的远程节点地址："',
'"h3",null,"URL Previews"':'"h3",null,"聊天信息中的超链接预览设置"',
'"label",null,"You have "':'"label",null,"当前 "',
'" URL previews by default."':'" 超链接预览功能"',
'getUrlPreviewsDisabled()?"disabled":"enabled"':'getUrlPreviewsDisabled()?"已经关闭":"已经启用"',
'"Permissions"':'"聊天室权限管理"',
'"The default role for new room members is "':'"新成员默认权限级别："',
'"To send messages, you must be a "':'"允许发送聊天消息的最低权限级别："',
'"To invite users into the room, you must be a "':'"允许邀请他人加入本聊天室的最低权限级别："',
'"To configure the room, you must be a "':'"允许修改聊天室配置的最低权限级别："',
'"To kick users, you must be a "':'"允许踢人的最低权限级别："',
'"To ban users, you must be a "':'"允许拉黑别人的最低权限级别："',
'"To redact messages, you must be a "':'"允许撤消聊天记录的最低权限级别："',
'"To send events of type "':'"若要修改 "',
'", you must be a "':'" ，你必须是 "',
'"This will make your account permanently unusable. You will not be able to re-register the same user ID."':'"销毁帐号将使你的当前帐号永久失效！并且不能使用相同的用户ID重新注册！"',
'"This action is irreversible."':'"销毁帐号的操作无法恢复！"',
'"To continue, please enter your password."':'"如要继续，请输入你的密码"',
'"Password:"':'"密码："',
'"Invalid Email Address"':'"非法的Email地址"',
'"This doesn\'t appear to be a valid email address"':'"你输入的Email地址无效，请重新输入"',
'"Disable URL previews by default for participants in this room"':'"为所有成员禁用超链接预览"',
'"Enable URL previews for this room (affects only you)"':'"只为我启用超链接预览（当前聊天室）"',
'"Disable URL previews for this room (affects only you)"':'"只为我禁用超链接预览（当前聊天室）"',
'"Privileged Users"':'"本聊天室的特权用户"',
'"Save"':'"保存"',
'"Manage Integrations"':'"管理桥接插件"',
'"Leave room"':'"离开聊天室"',
'"Are you sure you want to leave the room?"':'"你确定要离开当前聊天室吗？"',
'"Encryption is ",n?"":"not "," enabled in this room."':'"是否开启消息加密：",n?"":"没有 "," 开启"',
'"URL previews are ",this.state.globalDisableUrlPreview?"disabled":"enabled"," by default for participants in this room."':'"本聊天室的超链接预览功能默认为所有成员",this.state.globalDisableUrlPreview?"关闭":"开启"',
'"This room\'s internal ID is "':'"本聊天室的内部ID是："',
'"Filter room members"':'"搜索成员"',
'"Invite to this room"':'"邀请朋友加入此聊天室"',
'"Invite new room members"':'"邀请朋友加入当前聊天室"',
'"Who would you like to add to this room?"':'"请输入对方帐号信息"',
'"Send Invites"':'"发送邀请"',
'"Level: "':'"用户权限："',
'"Verify..."':'"信任"',
'"Blacklist"':'"拉黑"',
'"Unverify"':'"取消信任"',
'"Direct chats"':'"私聊选项"',
'"Start new chat"':'"开启新的私聊"',
'"Admin tools"':'"用户管理选项"',
'membership?"Disinvite":"Kick"':'membership?"取消邀请":"踢出聊天室"',
'onClick:this.onBan},"Ban"':'onClick:this.onBan},"拉黑该用户"',
'this.state.muted?"Unmute":"Mute"':'this.state.muted?"取消禁言":"禁言"',
'"Make Moderator"':'"将权限更改为 Moderator"',
'"Verify device"':'"信任该设备"',
'"To verify that this device can be trusted, please contact its owner using some other means (e.g. in person or a phone call) and ask them whether the key they see in their User Settings for this device matches the key below:"':'"请通过以下方式确认该设备属于对方本人：与对话手机通话或当面检查对方的设备ID与设备密钥和下面列出的信息一致"',
'"Device name:"':'"设备名称："',
'"If it matches, press the verify button below. If it doesnt, then someone else is intercepting this device and you probably want to press the blacklist button instead."':'"如果对方的信息与上述一致，请点击信任按钮，如果不一致，说明有人在冒充对方与你聊天，请立即拉黑该设备！"',
'"In future this verification process will be more sophisticated."':'"今后这一验证过程将会更加复杂（可靠）"',
'"I verify that the keys match"':'"我确认他的身份可信"',










}


# 执行字符替换
zh_strings = replace_words(en_strings, word_dic)

 
# 输出汉化后的js文件
fout = open(sourcefile,"w")
fout.write(zh_strings )
fout.close()
