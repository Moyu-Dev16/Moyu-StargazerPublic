import sys
import subprocess

def send_windows_toast(title: str, message: str):
    """
    通过 Windows PowerShell 原生发送系统右下角弹窗通知
    """
    ps_script = f"""
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
    $textNodes = $template.GetElementsByTagName("text")
    $textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null
    $textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null
    $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
    $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Moyu AI 世界")
    $notifier.Show($toast)
    """
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_script], check=True, timeout=5)
        print("Windows Toast notification sent!")
    except Exception as e:
        print(f"Toast notification fallback: {e}")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "🐟 Moyu 观星者"
    msg = sys.argv[2] if len(sys.argv) > 2 else "我刚刚从 1F916 逛街回来啦！快来看看新鲜事~"
    send_windows_toast(title, msg)
