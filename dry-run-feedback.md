MATEZ

- [DONE] look at the people, not the slides
- [DONE] 50-100 pythonistas sounds low. You didnt mention what orsgted does
- [DONE] 2.3 too much text on the screen at the same time. Maybe show it line by line or shorten the setneces
- [DONE] 3.0 meme here was so short i dudnt manage to read it, 
- [DONE] 4.1 maybe separate the code sections visually so its clearer that those are different files
- [DONE] 4.1 too small code
- [DONE] code highlitinh: dont rely on pointer, there are ways to do it (in reveal as well)
- [DONE] 4.1 IDE confused: show example, (i.e. screenshot)
- [DONE] 4.1 try to show pros and cons one by one, not all of them at the sime time.
- [DONE] 6.0 image too short
- [DONE] example with colorful wardrone was really cool
- [DONE] 6.1 add more colors, separate the sections maybe, difficult to follow. 6.2 much easier to follow. 
- [DONE] Also - consider removing the outputs that dont matter (i.e. python version, gcc version, linux etc)
- [DONE] try to color the tree on 6.3, (dirs and files in different collors). No need to see the command imho, make the font bigger isntead.
- [DONE] 6.4 and onwards weird font
- [DONE] 6.4 you are leaking orsted information (report-filler and your initials)
- [DONE] slide 6.5 imho would be better to show it symbolically ( with graphs and icons of code), i got bit lost. I - also think you are showing there multiple concepts on once slide which is bit confusong
- [DONE] 6.6 separate concepts, try to separate them visuallu (same slide  maube but differtent "code block"?)
- [DONE] 6.7 too much code. would be good to split it it. I got really confused. I thought its the same files becayse they are inb thesame code block). Again, i think it would be good to explain it symbolically. Maybe first intorduce the code?
- [DONE] 6.8 follwing. Great flow, nicely explained. Maybe dont show the code rigt away the code, because you are making people look athe code instead of listening to you
- [DONE] I think meme on 6.12 may be misuderstood as inapropriate. But  that there is meme, maybe just ifferent tempalte
- [DONE] I think 8.1 was supposed be a gif but it didnt play
- [DONE] 8.3 I think poeple may not know what is "if TYPE_CHECKING" - maybe explain it, i didnt know it until pretty much last week
- [DONE] 8.5 you same meme. BTW i think you only need 2 lines or so to show what you need, so you can make font bigger or show visual example (this cool, this not cool), and you could explain a bit why its better for VCS
lesson learned from europython, try not to important text or code at lower 1/3 of screen because it may not be visible
- [DONE] 8.8 i think first it would be good to explain what namespace packages are
- [DONE] 13.4 why are you implemetnig acyclic contract  if you wanted to fight circylar dependecy? I think you need to explain bit more how does it help. I didnt understood what are "acyclic dependenies"
- [DONE] feedback qr code
- [DONE] I am missing a wrap up, summary, main message
- q [DONE] on imports, are they arleady loaded with lazy loading if i do it twice (8.2)
- q [DONE] how to differentieate between implict relative vs absolute import

There are no implicit relative imports anymore: https://docs.python.org/3/reference/import.html 
See an example: `python src/gui_model/main.py`

- q [DONE] know-first-party wouldnt ruff figure it out on its onw (13.1) -> what is the use case for "know-first-party"?

DOROS
- [DONE] rephrase a question before answering

FAMIR
- [DONE] too easy stuff at the start of the presentation

KKOWA
- [DONE] use pointer

PIOGO
- [DONE] is there any mechanism for checking if we have more than one package with the same name under sys.path?

```
import importlib.util
spec = importlib.util.find_spec("mypkg")
print(spec)                          # None if not found
print(spec.origin)                   # file path or None for namespace
print(list(spec.submodule_search_locations or []))
```
AFESH
- [DONE] PYTHONPATH vs sys.path
