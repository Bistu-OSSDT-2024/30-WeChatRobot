package api;

import IdentifyCommand.PreProcessMessage;
import config.GlobalConfig;
import cons.WxMsg;

/**
 * Created by IntelliJ IDEA.
 *
 * @author Javior
 * @date 2019/6/20 16:10
 */
public class HelpMsg {

    private static final String README_LINK = GlobalConfig.getValue("helpMsg.detail", "https://github.com/scorego/WechatRobot");

    public static String getHelpMsg() {
        String commandPrefix = PreProcessMessage.getCommandPrefix();
        return "WeChat指令聊天机器人" + WxMsg.LINE
                + "【指令前缀】" + commandPrefix + WxMsg.LINE
                + "【天气查询】" + commandPrefix + "北京天气" + WxMsg.LINE
                + "【垃圾分类】" + commandPrefix + "？塑料袋" + WxMsg.LINE
                + "【当日新闻】" + commandPrefix + "新闻" + WxMsg.LINE
                + "【知乎热榜】" + commandPrefix + "知乎" + WxMsg.LINE
                + "【尝试一下】试着发一下\"" + PreProcessMessage.getCommandPrefix() + "？\"" + WxMsg.LINE
                + "【MORE】详情见" + README_LINK + WxMsg.LINE;
    }
}
