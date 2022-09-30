CJenkins
=======
CJenkins is a jenkins GUI in the terminal. It displays jobs and their status. You can also enter interactive mode where you can build the different jobs.

![](https://raw.github.com/mariushe/cjenkins/master/cjenkins.png)

#### How run:
`python cjenkins -u <username> -p <password> -l <jenkins 1 address> .. <jenkins n address>`

You can use the monitor without giving username and password. However, they are required to start builds.

#### Commands:
* `ctrl + c` to enter interactive mode

##### When in interactive mode
* `ctrl + c` to quit
* `w` to move up
* `s` to move down
* `b` build marked job
* `m` go back to monitor mode

I recommend to create an alias for cjenkins.

Here is an example:
`alias cjenkins="/<path>/cjenkins.py <url to jenkins>"`

#### Update:
Now you can add several jenkins' as arguments. That way you can get all your jenkins' in one window!

##### CJenkins' interactive mode:
![](https://raw.github.com/mariushe/cjenkins/master/interactivemode.png)

##### CJenkins with several jenkins':
![](https://raw.github.com/mariushe/cjenkins/master/cjenkinsWithSeveralJenkins.png)
