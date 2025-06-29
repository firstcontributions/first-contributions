# Git के माहौल सेट करीं

जब रउआ पहिला बेर Git में commit करे के कोशिश करब, त रउआ नीचे वाला संदेश देख सकत बानी:

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
config --global to set the identity only in this repository.
```

Git के पता होखे के चाहीं कि commit केहू बनावत बा। जब कई लोग एक साथ काम करत बा, त पता चले के चाहीं कि केहू कब, का बदलाव कइलस। एह खातिर, Git में हर commit के नाम आ ईमेल से जोड़ल जाला।

'git commit' में रउआ आपन नाम आ ईमेल कई तरीका से दे सकत बानी, नीचे कुछ तरीका बतावल गइल बा।

### Global Configuration

Global configuration में कुछ सेटिंग्स सेव कइला पर, ऊ हर repository में लागु हो जाला। ई तरीका सबसे बढ़िया बा आ ज्यादातर केस में काम करेला।

Global configuration में सेव करे खातिर 'config' कमांड इस्तेमाल करीं:

`$ git config --global <variable name> <value>`

यूजर डेटा खातिर:

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Repository Configuration

जइसन नाम से बुझात बा, ई सेटिंग्स खाली एके repository में लागु होखेला। अगर रउआ खास एक project में अलग email से commit करे चाहत बानी, त ई तरीका इस्तेमाल करीं।

Repository configuration में सेव करे खातिर, `config` कमांड से `--global` हटा दीं:

`$ git config <variable name> <value>`

यूजर डेटा खातिर:

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### Command Line Configuration

ई सेटिंग्स खाली ओही कमांड लाइन के आदेश खातिर लागु होखेला। Git के हर कमांड में `-c` prefix से अस्थायी configuration दे सकत बानी।

Command line configuration में इस्तेमाल करीं:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

हमार example में, commit कमांड ए तरह से इस्तेमाल होई:

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### Priority के बारे में

ऊपर बतावल तरीका के priority ई बा: `command-line > repository > global`। मतलब अगर variable command-line आ global दुनो में सेट बा, त command-line वाला मान इस्तेमाल होई।

## अउरी जानकारी

अबले हम user settings पर बात कइनी, बाकिर अउरी कुछ configuration भी बा। कुछ example:

1.  `core.editor` - कौन text editor से comment लिखब, ई सेट करे खातिर।
2.  `commit.template` - commit message के template फाइल सेट करे खातिर।
3.  `color.ui` - Git के output में रंग इस्तेमाल करे खातिर।

समुझावे खातिर कुछ बात आसान बनावल गइल बा। अउरी पढ़े खातिर देखीं [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
