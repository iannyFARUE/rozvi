from datetime import datetime, timezone as dt_timezone

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from blog.models import Post

User = get_user_model()

AUTHORS = {
    'ian-farai-madhara': 'Ian Farai Madhara',
    'naomi-chen': 'Naomi Chen',
    'marcus-webb': 'Marcus Webb',
    'priya-anand': 'Priya Anand',
    'sofia-delgado': 'Sofia Delgado',
}

POSTS = [
    {
        'title': 'Why Django Still Wins for Solo Developers in 2026',
        'excerpt': "Frameworks come and go, but Django's batteries-included "
                   "philosophy keeps paying off when you're shipping alone. "
                   "Here's what keeps me coming back to it for every side project.",
        'content': (
            "Every year a new framework promises to make backend development "
            "simpler, and every year I end up back at Django for anything I'm "
            "building alone.\n\n"
            "The batteries-included philosophy is the whole pitch: an ORM, an "
            "admin panel, authentication, and a migrations system that all agree "
            "with each other out of the box. When you're the only engineer on a "
            "project, the hours you don't spend gluing libraries together are "
            "hours you get to spend on the thing that actually makes your product "
            "different.\n\n"
            "None of this means Django is the right tool for every job. But for "
            "the class of project most solo developers are actually building — a "
            "CRUD app with a database behind it — it remains very hard to beat."
        ),
        'author_key': 'ian-farai-madhara',
        'topic': 'Software Engineering',
        'date_posted': datetime(2026, 9, 2, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 6,
        'claps_count': 482,
        'featured': True,
    },
    {
        'title': 'A Field Guide to Reading Other People’s Code',
        'excerpt': 'Most of your career will be spent inside codebases you '
                   'did not write. These are the habits that made me faster '
                   'at understanding unfamiliar systems.',
        'content': (
            "Most of your career will be spent inside codebases you did not "
            "write, which makes reading code a far more valuable skill than "
            "most curricula treat it as.\n\n"
            "The habit that changed things for me was resisting the urge to "
            "understand everything before touching anything. Instead, start "
            "from a single behavior you can observe, and trace only the path "
            "that produces it. You'll build a map of the system one thread at "
            "a time instead of trying to hold the whole thing in your head at "
            "once.\n\n"
            "Tests, when they exist, are the fastest map you'll find. They "
            "encode what the original author thought was worth protecting, "
            "which tells you more about intent than the implementation ever will."
        ),
        'author_key': 'naomi-chen',
        'topic': 'Career',
        'date_posted': datetime(2026, 8, 29, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 8,
        'claps_count': 915,
        'featured': True,
    },
    {
        'title': 'Postgres Indexes Explained With Pictures',
        'excerpt': 'B-trees, GIN, and BRIN indexes stop being scary once you '
                   'can see how they organize data on disk. A visual walkthrough '
                   'for backend developers.',
        'content': (
            "B-trees, GIN, and BRIN indexes stop being scary once you can see "
            "how they organize data on disk instead of just memorizing which "
            "CREATE INDEX syntax to reach for.\n\n"
            "A B-tree index is the default for a reason: it keeps rows sorted "
            "in a balanced tree so equality and range lookups both stay fast as "
            "the table grows. GIN indexes flip that around, mapping individual "
            "values back to the rows that contain them, which is why they excel "
            "at full-text search and array containment queries. BRIN indexes "
            "trade precision for size, storing only the min and max value per "
            "block, which works beautifully on naturally ordered data like "
            "timestamps.\n\n"
            "Once you can picture what each structure actually stores, choosing "
            "between them stops being guesswork."
        ),
        'author_key': 'marcus-webb',
        'topic': 'Databases',
        'date_posted': datetime(2026, 8, 24, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 11,
        'claps_count': 1204,
        'featured': True,
    },
    {
        'title': 'I Quit My Job to Write Full-Time. Here’s the Honest Update.',
        'excerpt': 'Six months, no salary, and a lot of self-doubt. A candid '
                   'look at what nobody tells you about leaving stability behind.',
        'content': (
            "Six months ago I left a stable job to write full-time. This is the "
            "honest update, not the highlight reel.\n\n"
            "The financial anxiety was exactly as bad as everyone warns you it "
            "will be, and no amount of runway math fully prepares you for "
            "watching a savings account only go down. What surprised me was the "
            "identity anxiety underneath it — how much of my sense of competence "
            "had been quietly borrowed from a job title.\n\n"
            "I don't have a tidy conclusion yet. What I have is a smaller, "
            "steadier readership than I expected, and a stubborn refusal to "
            "call this a mistake before the experiment is actually over."
        ),
        'author_key': 'priya-anand',
        'topic': 'Life',
        'date_posted': datetime(2026, 8, 20, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 5,
        'claps_count': 2310,
        'featured': False,
    },
    {
        'title': 'Designing APIs People Actually Enjoy Using',
        'excerpt': 'Good API design is invisible — it just feels obvious. '
                   'A breakdown of the small decisions that separate a delightful '
                   'SDK from a frustrating one.',
        'content': (
            "Good API design is invisible — it just feels obvious in hindsight, "
            "which is exactly why it's so easy to underrate.\n\n"
            "The small decisions matter more than the big ones: consistent "
            "naming across every endpoint, error messages that tell you what to "
            "do next instead of just what went wrong, and defaults that match "
            "what most callers actually want. None of these show up in a feature "
            "list, but they're the difference between an SDK that developers "
            "recommend and one they merely tolerate.\n\n"
            "If you want to know whether your API is well designed, watch "
            "someone use it for the first time without helping them."
        ),
        'author_key': 'ian-farai-madhara',
        'topic': 'Software Engineering',
        'date_posted': datetime(2026, 8, 15, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 7,
        'claps_count': 671,
        'featured': False,
    },
    {
        'title': 'The Case for Boring Technology',
        'excerpt': 'Chasing the newest framework has a cost that rarely shows '
                   'up in the demo. Why picking the dull, proven tool is usually '
                   'the ambitious choice.',
        'content': (
            "Chasing the newest framework has a cost that rarely shows up in "
            "the demo: the debugging time, the missing documentation, and the "
            "hiring pool that hasn't caught up yet.\n\n"
            "Boring technology has already had its edge cases found by someone "
            "else. That's not a lack of ambition — it's redirecting your ambition "
            "toward the actual problem instead of the tools you're using to "
            "solve it.\n\n"
            "Save the novelty budget for the one part of the system that's "
            "actually new. Everything else should be as dull as you can get "
            "away with."
        ),
        'author_key': 'sofia-delgado',
        'topic': 'Opinion',
        'date_posted': datetime(2026, 8, 9, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 4,
        'claps_count': 389,
        'featured': False,
    },
    {
        'title': 'What Building in Public Actually Taught Me',
        'excerpt': 'A year of sharing unfinished work, failed launches, and '
                   'small wins online. The lessons had very little to do with marketing.',
        'content': (
            "A year of sharing unfinished work, failed launches, and small wins "
            "online taught me a lot less about marketing than I expected, and a "
            "lot more about finishing things.\n\n"
            "Knowing that a post about progress is due at the end of the week "
            "turns out to be a surprisingly effective forcing function. It's "
            "harder to let a project quietly die when you've already told people "
            "it exists.\n\n"
            "The audience that showed up mattered less than the accountability "
            "of having one at all."
        ),
        'author_key': 'marcus-webb',
        'topic': 'Startups',
        'date_posted': datetime(2026, 8, 3, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 9,
        'claps_count': 1560,
        'featured': False,
    },
    {
        'title': 'Async Python Without the Headaches',
        'excerpt': 'asyncio has a reputation for being confusing. Once you '
                   'understand the event loop as a single idea, the rest clicks '
                   'into place.',
        'content': (
            "asyncio has a reputation for being confusing, but most of that "
            "confusion comes from learning the syntax before the model it's "
            "built on.\n\n"
            "Once you understand the event loop as a single idea — one thread, "
            "juggling many tasks by switching between them at every `await` — "
            "the rest of the API stops feeling arbitrary. Coroutines aren't "
            "magic; they're just functions that know how to pause.\n\n"
            "Start there, and concepts like gather, tasks, and cancellation "
            "start to feel like consequences of that one idea rather than a "
            "pile of new vocabulary to memorize."
        ),
        'author_key': 'naomi-chen',
        'topic': 'Python',
        'date_posted': datetime(2026, 7, 27, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 10,
        'claps_count': 843,
        'featured': False,
    },
    {
        'title': 'Why I Stopped Taking Notes During Meetings',
        'excerpt': 'Writing everything down felt productive. It was actually '
                   'costing me the one thing meetings are supposed to produce: '
                   'a decision.',
        'content': (
            "Writing everything down felt productive. It was actually costing "
            "me the one thing most meetings are supposed to produce: a decision "
            "everyone in the room actually agreed to.\n\n"
            "Note-taking gave my hands something to do while my attention drifted "
            "to the next bullet point instead of the person talking. Once I put "
            "the notebook away and just listened, I started noticing when a "
            "conversation was circling instead of converging — and said so.\n\n"
            "Now I write exactly one thing per meeting: the decision, and who "
            "owns the next step. Everything else was never going to get read again."
        ),
        'author_key': 'naomi-chen',
        'topic': 'Productivity',
        'date_posted': datetime(2026, 7, 20, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 4,
        'claps_count': 512,
        'featured': False,
    },
    {
        'title': 'The Undo Button Problem in Product Design',
        'excerpt': 'Most destructive actions in software still ask "are you sure?" '
                   'instead of just letting you undo. The difference matters more '
                   'than it looks.',
        'content': (
            "Most destructive actions in software still ask 'are you sure?' "
            "instead of just letting you undo. The difference looks small and "
            "isn't.\n\n"
            "A confirmation dialog interrupts you before you've finished the "
            "thought, so people learn to click through it on autopilot. An undo "
            "button lets the action happen, then gives you a real, low-stakes "
            "window to change your mind after you've actually seen the result.\n\n"
            "If a feature is important enough to protect, it's important enough "
            "to protect with something better than a modal nobody reads."
        ),
        'author_key': 'marcus-webb',
        'topic': 'Opinion',
        'date_posted': datetime(2026, 7, 13, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 5,
        'claps_count': 734,
        'featured': False,
    },
    {
        'title': "Caching Is Easy Until It Isn't",
        'excerpt': 'Adding a cache is a five-minute change. Keeping it correct '
                   'under real traffic is the part nobody warns you about.',
        'content': (
            "Adding a cache is a five-minute change: wrap the slow call, set a "
            "TTL, ship it. Keeping it correct under real traffic is the part "
            "nobody warns you about.\n\n"
            "Every cache eventually asks you the same question: what happens "
            "when the underlying data changes before the TTL expires? "
            "Invalidation strategies range from 'wait it out' to elaborate "
            "event-driven busting, and picking the wrong one for your access "
            "pattern is how you end up debugging a bug that only reproduces on "
            "Tuesdays.\n\n"
            "Start with the simplest strategy that tolerates being wrong for a "
            "few seconds. Most systems can afford that far more often than they "
            "can afford the complexity of the alternative."
        ),
        'author_key': 'ian-farai-madhara',
        'topic': 'Software Engineering',
        'date_posted': datetime(2026, 7, 6, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 6,
        'claps_count': 891,
        'featured': False,
    },
    {
        'title': 'What Five Years of Freelancing Taught Me About Saying No',
        'excerpt': 'Every yes to a project is a quiet no to something else. It '
                   'took me years of overcommitting to actually believe that.',
        'content': (
            "Every yes to a project is a quiet no to something else — usually "
            "the next client, the good ones, who ask when you're already fully "
            "booked and unwilling to admit it.\n\n"
            "For a long time I said yes to everything because turning down work "
            "felt like turning down income, full stop. What actually happened "
            "was slower delivery, more mistakes, and a reputation for being "
            "stretched thin rather than in demand.\n\n"
            "Saying no early, clearly, and without a guilty over-explanation "
            "turned out to be the more professional move, not the riskier one."
        ),
        'author_key': 'sofia-delgado',
        'topic': 'Career',
        'date_posted': datetime(2026, 6, 29, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 5,
        'claps_count': 1023,
        'featured': False,
    },
    {
        'title': 'The Small Talk I Actually Miss From the Office',
        'excerpt': "Remote work fixed most of what I hated about commuting. It "
                   "also quietly removed the conversations I didn't know I needed.",
        'content': (
            "Remote work fixed most of what I hated about commuting. It also "
            "quietly removed a category of conversation I didn't know I needed "
            "until it was gone.\n\n"
            "The five minutes waiting for coffee, the aside after a meeting "
            "technically ended — those weren't wasted time, they were where half "
            "the actual context about a project used to travel. Slack threads "
            "are a poor substitute; they require someone to already believe the "
            "information is worth typing out.\n\n"
            "I don't want the commute back. I do think we underrated how much "
            "of a team's shared understanding was never actually written down "
            "anywhere on purpose."
        ),
        'author_key': 'priya-anand',
        'topic': 'Life',
        'date_posted': datetime(2026, 6, 22, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 4,
        'claps_count': 1487,
        'featured': False,
    },
    {
        'title': "A Beginner's Guide to Database Migrations",
        'excerpt': 'Migrations feel intimidating right up until you understand '
                   'that they are just version control for your schema.',
        'content': (
            "Migrations feel intimidating right up until you understand that "
            "they are, at their core, just version control for your schema.\n\n"
            "Each migration is a small, ordered, reversible change: add this "
            "column, backfill that data, drop this old table once nothing reads "
            "from it anymore. The framework's job is just to track which of "
            "those changes have already been applied to a given database, the "
            "same way git tracks which commits are already on a branch.\n\n"
            "The habit that saves you the most pain is keeping migrations small "
            "and running them constantly, the same way small, frequent commits "
            "save you from painful merges."
        ),
        'author_key': 'marcus-webb',
        'topic': 'Databases',
        'date_posted': datetime(2026, 6, 15, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 7,
        'claps_count': 658,
        'featured': False,
    },
    {
        'title': "Type Hints Won't Save a Bad API, But They Help",
        'excerpt': "Type hints don't make Python fast or safe by themselves. "
                   "What they actually buy you is a much shorter feedback loop.",
        'content': (
            "Type hints don't make Python fast or safe by themselves — the "
            "interpreter mostly ignores them at runtime. What they actually buy "
            "you is a much shorter feedback loop between writing a mistake and "
            "seeing it.\n\n"
            "A function signature that says what it expects and what it returns "
            "turns your editor into a collaborator instead of a text box. That "
            "matters more as a codebase grows past the size one person can hold "
            "in their head.\n\n"
            "They're not a substitute for tests, and they won't rescue a "
            "genuinely confusing API. But paired with a decent design, they make "
            "that design much harder to misuse by accident."
        ),
        'author_key': 'naomi-chen',
        'topic': 'Python',
        'date_posted': datetime(2026, 6, 8, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 6,
        'claps_count': 720,
        'featured': False,
    },
    {
        'title': 'Why I Write Design Docs Before Code',
        'excerpt': 'A design doc is cheaper to throw away than a pull request. '
                   'That alone is reason enough to write one first.',
        'content': (
            "A design doc is cheaper to throw away than a pull request, and "
            "that alone is reason enough to write one before touching an "
            "editor.\n\n"
            "Putting a plan in prose forces you to notice the parts you were "
            "hand-waving past — the edge case you hadn't picked a behavior for, "
            "the dependency you assumed would just work. Reviewers catch these "
            "far more cheaply in a paragraph than in a thousand lines of diff.\n\n"
            "The doc doesn't need to be long or formal. It just needs to exist "
            "long enough for someone else to poke a hole in it before the code does."
        ),
        'author_key': 'ian-farai-madhara',
        'topic': 'Software Engineering',
        'date_posted': datetime(2026, 6, 1, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 5,
        'claps_count': 601,
        'featured': False,
    },
    {
        'title': 'The Myth of the 10x Engineer',
        'excerpt': 'The most productive engineers I know are not typing faster '
                   'than everyone else. They are just causing far fewer problems.',
        'content': (
            "The most productive engineers I know are not typing faster than "
            "everyone else, or holding more of the codebase in their head. "
            "They are just causing far fewer problems for the people around "
            "them.\n\n"
            "That shows up as clear commit messages, pull requests scoped to one "
            "idea, and a habit of leaving a system slightly easier to understand "
            "than they found it. None of that is a superpower. It's closer to "
            "tidiness, applied consistently over years.\n\n"
            "If a '10x engineer' exists, the multiplier is on the team around "
            "them, not on their own output."
        ),
        'author_key': 'sofia-delgado',
        'topic': 'Opinion',
        'date_posted': datetime(2026, 5, 25, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 4,
        'claps_count': 1890,
        'featured': False,
    },
    {
        'title': 'How I Finally Learned to Ship Unfinished Work',
        'excerpt': "Waiting until something felt done meant almost nothing ever "
                   "shipped. Lowering the bar on purpose is what actually fixed it.",
        'content': (
            "Waiting until something felt done meant almost nothing ever "
            "shipped. What actually fixed it was lowering the bar on purpose, "
            "not raising my discipline.\n\n"
            "I started asking a smaller question before every release: is this "
            "honest and useful right now, even if it's incomplete? A rough "
            "version answering that in the affirmative beats a polished version "
            "that never leaves a draft folder.\n\n"
            "Feedback from something real in someone else's hands taught me more "
            "in a week than another month of solo polishing ever did."
        ),
        'author_key': 'priya-anand',
        'topic': 'Startups',
        'date_posted': datetime(2026, 5, 18, 9, 0, tzinfo=dt_timezone.utc),
        'read_time': 5,
        'claps_count': 947,
        'featured': False,
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with demo authors and blog posts for local development.'

    def handle(self, *args, **options):
        users = {}
        for username, full_name in AUTHORS.items():
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'first_name': full_name},
            )
            users[username] = user
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created user "{username}"'))

        for data in POSTS:
            author = users[data['author_key']]
            post, created = Post.objects.update_or_create(
                title=data['title'],
                author=author,
                defaults={
                    'excerpt': data['excerpt'],
                    'content': data['content'],
                    'topic': data['topic'],
                    'date_posted': data['date_posted'],
                    'read_time': data['read_time'],
                    'claps_count': data['claps_count'],
                    'featured': data['featured'],
                },
            )
            verb = 'Created' if created else 'Updated'
            self.stdout.write(self.style.SUCCESS(f'{verb} post "{post.title}"'))

        self.stdout.write(self.style.SUCCESS('Done seeding blog posts.'))
