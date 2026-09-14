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
