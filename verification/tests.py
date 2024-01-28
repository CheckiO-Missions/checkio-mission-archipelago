"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(
    (0, 1, 0, 0, 2),
    (2, 0, 0, 2, 0),
    (0, 0, 2, 0, 2),
    (0, 0, 0, 1, 0),
    (3, 0, 6, 0, 3)
)],
            "answer": (
    (1, 2, 1),
    (2, 6, 1),
    (3, 4, 1),
    (3, 8, 1),
    (4, 7, 1),
    (5, 9, 2),
    (6, 10, 1),
    (8, 9, 2),
    (9, 10, 2)
),
            "explanation": "very easy, 5x5"
        },
        {
            "input": [(
    (3, 0, 6, 0, 3),
    (0, 1, 0, 0, 0),
    (2, 0, 2, 0, 0),
    (0, 2, 0, 0, 3),
    (5, 0, 3, 0, 0),
    (0, 0, 0, 0, 1),
    (2, 0, 1, 0, 0)
)],
            "answer": (
    (1, 2, 2),
    (1, 5, 1),
    (2, 3, 2),
    (2, 6, 2),
    (3, 8, 1),
    (4, 7, 1),
    (5, 9, 1),
    (7, 8, 1),
    (8, 11, 1),
    (9, 10, 2),
    (9, 12, 2),
    (10, 13, 1)
 ),
            "explanation": "very easy, 5x7"
        },
        {
            "input": [(
    (0, 2, 0, 0, 2, 0),
    (2, 0, 2, 0, 0, 0),
    (0, 1, 0, 0, 0, 2),
    (5, 0, 8, 0, 3, 0),
    (0, 0, 0, 0, 0, 0),
    (1, 0, 3, 0, 0, 3)
)],
            "answer": (
    (1, 2, 1),
    (1, 5, 1),
    (2, 9, 1),
    (3, 7, 2),
    (4, 8, 2),
    (6, 12, 2),
    (7, 8, 2),
    (7, 10, 1),
    (8, 9, 2),
    (8, 11, 2),
    (11, 12, 1)
 ),
            "explanation": "very easy, 6x6"
        },
    ],
    "Extra": [
        {
            "input": [(
    (2, 0, 0, 3, 0, 0),
    (0, 1, 0, 0, 0, 1),
    (2, 0, 0, 0, 0, 0),
    (0, 4, 0, 8, 0, 4),
    (2, 0, 1, 0, 0, 0),
    (0, 2, 0, 2, 0, 0),
    (1, 0, 2, 0, 0, 2),
    (0, 2, 0, 0, 1, 0)
)],
            "answer": (
    (1, 2, 1),
    (1, 5, 1),
    (2, 7, 2),
    (3, 6, 1),
    (4, 8, 1),
    (5, 9, 1),
    (6, 7, 2),
    (6, 11, 1),
    (7, 8, 2),
    (7, 12, 2),
    (8, 15, 1),
    (9, 13, 1),
    (10, 14, 1),
    (11, 16, 1),
    (14, 15, 1),
    (16, 17, 1)
 ),
            "explanation": "very easy, 6x8"
        },
        {
            "input": [(
    (2, 0, 3, 0, 6, 0, 2),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 0, 8, 0, 3),
    (0, 0, 0, 0, 0, 0, 0),
    (2, 0, 0, 2, 0, 0, 1),
    (0, 0, 0, 0, 2, 0, 0),
    (0, 2, 0, 5, 0, 0, 2)
)],
            "answer": (
    (1, 2, 1),
    (1, 8, 1),
    (2, 3, 2),
    (3, 4, 2),
    (3, 6, 2),
    (5, 6, 2),
    (6, 7, 2),
    (6, 11, 2),
    (7, 10, 1),
    (8, 9, 1),
    (9, 13, 1),
    (12, 13, 2),
    (13, 14, 2)
 ),
            "explanation": "very easy, 7x7"
        },
        {
            "input": [(
    (2, 0, 2, 0, 1, 0, 0),
    (0, 2, 0, 5, 0, 0, 2),
    (4, 0, 1, 0, 0, 2, 0),
    (0, 0, 0, 0, 0, 0, 2),
    (5, 0, 0, 8, 0, 5, 0),
    (0, 1, 0, 0, 2, 0, 0),
    (1, 0, 0, 2, 0, 0, 2),
    (0, 0, 0, 0, 0, 1, 0),
    (0, 3, 0, 0, 6, 0, 3)
)],
            "answer": (
    (1, 2, 1),
    (1, 7, 1),
    (2, 3, 1),
    (4, 5, 2),
    (5, 6, 1),
    (5, 12, 2),
    (6, 10, 1),
    (7, 8, 1),
    (7, 11, 2),
    (9, 13, 2),
    (10, 18, 1),
    (11, 12, 2),
    (11, 16, 1),
    (12, 13, 2),
    (12, 17, 2),
    (13, 19, 1),
    (14, 20, 1),
    (15, 21, 2),
    (18, 22, 1),
    (20, 21, 2),
    (21, 22, 2)
 ),
            "explanation": "very easy, 7x9"
        },
        {
            "input": [(
    (1, 0, 2, 0, 5, 0, 1, 0),
    (0, 0, 0, 0, 0, 1, 0, 2),
    (4, 0, 5, 0, 8, 0, 2, 0),
    (0, 0, 0, 0, 0, 2, 0, 4),
    (3, 0, 4, 0, 8, 0, 4, 0),
    (0, 0, 0, 1, 0, 1, 0, 2),
    (0, 0, 1, 0, 3, 0, 3, 0),
    (4, 0, 0, 2, 0, 2, 0, 2),
    (0, 0, 2, 0, 3, 0, 1, 0),
    (2, 0, 0, 2, 0, 3, 0, 2)
)],
            "answer": (
    (1, 7, 1),
    (2, 3, 2),
    (3, 4, 1),
    (3, 9, 2),
    (5, 6, 1),
    (6, 12, 1),
    (7, 8, 2),
    (7, 13, 1),
    (8, 9, 2),
    (8, 14, 1),
    (9, 10, 2),
    (9, 15, 2),
    (11, 12, 2),
    (12, 19, 1),
    (13, 23, 2),
    (14, 15, 2),
    (14, 20, 1),
    (15, 16, 2),
    (15, 21, 2),
    (16, 22, 2),
    (17, 24, 1),
    (18, 25, 1),
    (19, 26, 1),
    (21, 28, 1),
    (22, 29, 1),
    (23, 24, 1),
    (23, 30, 1),
    (25, 32, 1),
    (26, 33, 1),
    (27, 28, 2),
    (30, 31, 1),
    (31, 32, 1),
    (32, 33, 1)
 ),
            "explanation": "very easy, 8x10"
        },
        {
            "input": [(
    (3, 0, 2, 0, 4, 0, 1),
    (0, 0, 0, 1, 0, 0, 0),
    (4, 0, 3, 0, 3, 0, 2),
    (0, 0, 0, 2, 0, 2, 0),
    (5, 0, 8, 0, 3, 0, 2),
    (0, 1, 0, 0, 0, 3, 0),
    (3, 0, 2, 0, 2, 0, 2),
    (0, 0, 0, 0, 0, 3, 0),
    (0, 3, 0, 0, 3, 0, 1),
    (3, 0, 0, 3, 0, 2, 0)
)],
            "answer": (
    (1, 2, 1),
    (1, 6, 2),
    (2, 3, 1),
    (3, 4, 1),
    (3, 8, 2),
    (5, 10, 1),
    (6, 7, 1),
    (6, 12, 1),
    (7, 13, 2),
    (8, 9, 1),
    (9, 15, 1),
    (10, 11, 1),
    (11, 17, 1),
    (12, 13, 2),
    (12, 18, 2),
    (13, 14, 2),
    (13, 19, 2),
    (14, 20, 1),
    (15, 21, 1),
    (16, 23, 1),
    (17, 22, 2),
    (18, 26, 1),
    (20, 24, 1),
    (21, 25, 1),
    (22, 28, 1),
    (23, 24, 2),
    (26, 27, 2),
    (27, 28, 1)
 ),
            "explanation": "easy, 7x10"
        },
        {
            "input": [(
    (0, 3, 0, 3, 0, 3, 0, 3),
    (2, 0, 1, 0, 2, 0, 0, 0),
    (0, 3, 0, 2, 0, 0, 1, 0),
    (6, 0, 2, 0, 0, 1, 0, 3),
    (0, 2, 0, 0, 4, 0, 3, 0),
    (0, 0, 0, 2, 0, 0, 0, 3),
    (4, 0, 0, 0, 2, 0, 0, 0),
    (0, 3, 0, 4, 0, 0, 2, 0),
    (3, 0, 2, 0, 3, 0, 0, 3),
    (0, 0, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 0, 3, 0, 0, 2)
)],
            "answer": (
    (1, 2, 2),
    (1, 8, 1),
    (2, 3, 1),
    (3, 4, 1),
    (3, 13, 1),
    (4, 14, 2),
    (5, 11, 2),
    (6, 7, 1),
    (7, 16, 1),
    (8, 9, 2),
    (10, 17, 1),
    (11, 12, 2),
    (11, 20, 2),
    (14, 19, 1),
    (15, 16, 1),
    (15, 22, 1),
    (16, 17, 1),
    (16, 21, 1),
    (17, 24, 1),
    (18, 23, 2),
    (19, 28, 2),
    (20, 25, 2),
    (21, 27, 1),
    (22, 23, 2),
    (24, 29, 1),
    (25, 26, 1),
    (26, 27, 1),
    (27, 31, 1),
    (28, 32, 1),
    (30, 31, 1),
    (31, 32, 1)
 ),
            "explanation": "easy, 8x11"
        },
        {
            "input": [(
    (2, 0, 6, 0, 3, 0, 0, 0, 2),
    (0, 0, 0, 1, 0, 0, 2, 0, 0),
    (2, 0, 0, 0, 0, 0, 0, 0, 3),
    (0, 0, 3, 0, 3, 0, 3, 0, 0),
    (5, 0, 0, 4, 0, 0, 0, 2, 0),
    (0, 0, 0, 0, 0, 2, 0, 0, 3),
    (0, 3, 0, 4, 0, 0, 0, 2, 0),
    (0, 0, 2, 0, 0, 0, 2, 0, 0),
    (3, 0, 0, 3, 0, 3, 0, 0, 3),
    (0, 0, 4, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 3, 0, 0, 7, 0, 3),
    (3, 0, 4, 0, 1, 0, 0, 0, 0),
    (0, 2, 0, 3, 0, 0, 4, 0, 1)
)],
            "answer": (
    (1, 2, 2),
    (2, 3, 2),
    (2, 9, 2),
    (3, 4, 1),
    (4, 8, 1),
    (5, 6, 1),
    (6, 11, 1),
    (7, 12, 2),
    (8, 16, 2),
    (9, 10, 1),
    (10, 11, 2),
    (12, 13, 2),
    (12, 22, 1),
    (13, 14, 1),
    (13, 18, 1),
    (14, 19, 1),
    (15, 24, 2),
    (16, 25, 1),
    (17, 18, 2),
    (17, 28, 1),
    (18, 23, 1),
    (19, 27, 1),
    (20, 26, 2),
    (21, 30, 2),
    (22, 32, 2),
    (23, 24, 1),
    (23, 29, 1),
    (25, 31, 2),
    (26, 33, 2),
    (29, 30, 2),
    (30, 31, 1),
    (30, 37, 2),
    (32, 33, 1),
    (33, 34, 1),
    (35, 36, 2),
    (36, 37, 1),
    (37, 38, 1)
 ),
            "explanation": "easy, 9x13"
        },
        {
            "input": [(
    (2, 0, 4, 0, 4, 0, 3, 0, 2, 0),
    (0, 0, 0, 2, 0, 4, 0, 3, 0, 0),
    (5, 0, 8, 0, 4, 0, 2, 0, 0, 1),
    (0, 1, 0, 0, 0, 0, 0, 0, 2, 0),
    (2, 0, 4, 0, 5, 0, 0, 4, 0, 3),
    (0, 3, 0, 1, 0, 0, 0, 0, 1, 0),
    (2, 0, 0, 0, 0, 2, 0, 5, 0, 4),
    (0, 0, 3, 0, 8, 0, 2, 0, 0, 0),
    (2, 0, 0, 0, 0, 1, 0, 0, 2, 0),
    (0, 2, 0, 0, 5, 0, 0, 2, 0, 0),
    (2, 0, 1, 0, 0, 0, 0, 0, 0, 2),
    (0, 3, 0, 0, 6, 0, 0, 0, 3, 0),
    (3, 0, 2, 0, 0, 0, 0, 0, 0, 1),
    (0, 1, 0, 0, 3, 0, 2, 0, 3, 0)
)],
            "answer": (
    (1, 9, 2),
    (2, 3, 2),
    (2, 10, 2),
    (3, 4, 2),
    (4, 5, 1),
    (5, 15, 1),
    (6, 7, 2),
    (7, 8, 2),
    (8, 19, 1),
    (9, 10, 2),
    (9, 16, 1),
    (10, 11, 2),
    (10, 17, 2),
    (11, 12, 2),
    (13, 20, 1),
    (14, 21, 1),
    (15, 23, 1),
    (16, 24, 1),
    (17, 18, 2),
    (18, 19, 1),
    (18, 29, 2),
    (19, 26, 2),
    (20, 27, 2),
    (21, 22, 1),
    (21, 34, 1),
    (24, 31, 1),
    (25, 26, 2),
    (26, 27, 1),
    (27, 39, 1),
    (28, 29, 2),
    (28, 38, 1),
    (29, 30, 2),
    (29, 35, 2),
    (31, 37, 1),
    (32, 33, 1),
    (33, 42, 1),
    (34, 40, 1),
    (35, 36, 2),
    (35, 41, 1),
    (37, 43, 1),
    (39, 45, 1),
    (40, 41, 2),
    (41, 42, 1),
    (41, 47, 2),
    (42, 49, 1),
    (43, 44, 2),
    (46, 47, 1),
    (48, 49, 2)
 ),
            "explanation": "easy, 10x14"
        },
        {
            "input": [(
    (0, 3, 0, 0, 4, 0, 2, 0),
    (2, 0, 0, 0, 0, 0, 0, 2),
    (0, 2, 0, 3, 0, 0, 1, 0),
    (0, 0, 0, 0, 2, 0, 0, 4),
    (5, 0, 0, 4, 0, 0, 2, 0),
    (0, 1, 0, 0, 3, 0, 0, 0),
    (4, 0, 0, 1, 0, 0, 0, 3),
    (0, 2, 0, 0, 3, 0, 5, 0),
    (0, 0, 0, 2, 0, 1, 0, 3),
    (2, 0, 0, 0, 1, 0, 3, 0),
    (0, 2, 0, 3, 0, 2, 0, 3)
)],
            "answer": (
    (1, 2, 2),
    (1, 6, 1),
    (2, 3, 1),
    (2, 9, 1),
    (3, 8, 1),
    (4, 11, 2),
    (5, 10, 2),
    (6, 7, 1),
    (7, 12, 2),
    (9, 15, 1),
    (10, 18, 2),
    (11, 12, 2),
    (11, 16, 1),
    (13, 21, 2),
    (14, 15, 1),
    (15, 20, 1),
    (16, 17, 1),
    (16, 25, 2),
    (18, 24, 1),
    (19, 20, 1),
    (19, 28, 1),
    (20, 21, 1),
    (21, 27, 2),
    (22, 23, 1),
    (22, 29, 1),
    (24, 31, 2),
    (26, 27, 1),
    (28, 29, 1),
    (29, 30, 1),
    (30, 31, 1)
 ),
            "explanation": "medium, 8x11"
        },
        {
            "input": [(
    (3, 0, 4, 0, 4, 0, 1, 0, 0),
    (0, 1, 0, 0, 0, 3, 0, 0, 2),
    (0, 0, 0, 0, 3, 0, 1, 0, 0),
    (3, 0, 2, 0, 0, 3, 0, 0, 0),
    (0, 3, 0, 0, 2, 0, 3, 0, 3),
    (3, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 3, 0, 2, 0, 0, 2),
    (3, 0, 0, 0, 1, 0, 2, 0, 0),
    (0, 3, 0, 3, 0, 0, 0, 0, 4),
    (2, 0, 2, 0, 0, 4, 0, 2, 0),
    (0, 2, 0, 1, 0, 0, 0, 0, 3),
    (3, 0, 2, 0, 0, 0, 0, 1, 0),
    (0, 2, 0, 4, 0, 3, 0, 0, 2)
)],
            "answer": (
    (1, 2, 1),
    (1, 10, 2),
    (2, 3, 1),
    (2, 11, 2),
    (3, 4, 1),
    (3, 8, 2),
    (5, 13, 1),
    (6, 7, 1),
    (6, 12, 2),
    (7, 16, 1),
    (8, 14, 1),
    (9, 15, 1),
    (10, 17, 1),
    (12, 20, 1),
    (13, 14, 1),
    (13, 18, 1),
    (15, 16, 1),
    (15, 24, 1),
    (16, 21, 1),
    (17, 22, 2),
    (18, 19, 1),
    (19, 20, 1),
    (19, 26, 1),
    (21, 27, 1),
    (22, 28, 1),
    (23, 24, 1),
    (25, 26, 1),
    (25, 32, 2),
    (26, 27, 1),
    (27, 34, 2),
    (28, 35, 1),
    (29, 30, 2),
    (30, 31, 1),
    (30, 40, 1),
    (31, 37, 1),
    (33, 39, 1),
    (34, 41, 1),
    (35, 36, 2),
    (38, 39, 2),
    (39, 40, 1),
    (40, 41, 1)
 ),
            "explanation": "medium, 9x13"
        },
        {
            "input": [(
    (0, 3, 0, 3, 0, 4, 0, 4, 0, 3),
    (2, 0, 0, 0, 2, 0, 1, 0, 0, 0),
    (0, 5, 0, 3, 0, 2, 0, 0, 2, 0),
    (3, 0, 0, 0, 0, 0, 0, 2, 0, 3),
    (0, 4, 0, 0, 6, 0, 3, 0, 4, 0),
    (2, 0, 0, 0, 0, 0, 0, 0, 0, 2),
    (0, 4, 0, 2, 0, 2, 0, 0, 4, 0),
    (2, 0, 1, 0, 0, 0, 0, 0, 0, 3),
    (0, 1, 0, 0, 3, 0, 0, 1, 0, 0),
    (0, 0, 0, 3, 0, 2, 0, 0, 0, 3),
    (3, 0, 3, 0, 4, 0, 3, 0, 2, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (2, 0, 0, 1, 0, 2, 0, 3, 0, 2),
    (0, 0, 2, 0, 4, 0, 3, 0, 2, 0)
)],
            "answer": (
    (1, 2, 1),
    (1, 9, 2),
    (2, 3, 1),
    (2, 10, 1),
    (3, 4, 1),
    (3, 11, 2),
    (4, 5, 1),
    (4, 14, 2),
    (5, 15, 2),
    (6, 13, 2),
    (7, 17, 2),
    (8, 18, 1),
    (9, 10, 2),
    (9, 16, 1),
    (12, 19, 2),
    (13, 20, 1),
    (15, 21, 1),
    (16, 17, 1),
    (16, 22, 2),
    (17, 18, 1),
    (17, 30, 2),
    (18, 19, 1),
    (19, 25, 1),
    (20, 26, 1),
    (21, 28, 1),
    (22, 23, 1),
    (22, 29, 1),
    (23, 32, 1),
    (24, 25, 2),
    (25, 39, 1),
    (26, 35, 1),
    (27, 36, 1),
    (28, 34, 2),
    (30, 31, 1),
    (32, 33, 2),
    (34, 44, 1),
    (35, 36, 1),
    (35, 40, 1),
    (36, 37, 1),
    (37, 38, 2),
    (37, 46, 1),
    (38, 39, 1),
    (40, 41, 1),
    (42, 43, 2),
    (43, 44, 1),
    (45, 46, 2),
    (46, 47, 1),
    (47, 48, 2)
 ),
            "explanation": "medium, 10x14"
        },
        {
            "input": [(
    (0, 2, 0, 0, 5, 0, 0, 2, 0),
    (0, 0, 0, 0, 0, 2, 0, 0, 3),
    (2, 0, 2, 0, 3, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 0, 4, 0, 3, 0, 2),
    (3, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 2, 0, 0, 2, 0, 3, 0, 1),
    (0, 0, 0, 2, 0, 0, 0, 0, 0),
    (2, 0, 0, 0, 2, 0, 3, 0, 2),
    (0, 4, 0, 6, 0, 3, 0, 1, 0),
    (2, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 2, 0, 0, 2, 0, 3),
    (2, 0, 4, 0, 0, 5, 0, 2, 0)
)],
            "answer": (
    (1, 2, 2),
    (2, 3, 2),
    (2, 8, 1),
    (4, 5, 2),
    (5, 13, 1),
    (6, 7, 1),
    (6, 14, 1),
    (7, 8, 1),
    (8, 11, 1),
    (9, 12, 1),
    (10, 11, 2),
    (11, 17, 1),
    (12, 13, 1),
    (12, 18, 1),
    (14, 15, 1),
    (14, 21, 1),
    (16, 25, 2),
    (17, 22, 1),
    (18, 19, 1),
    (18, 23, 1),
    (20, 26, 2),
    (21, 29, 1),
    (22, 23, 1),
    (23, 24, 1),
    (24, 34, 1),
    (25, 26, 1),
    (25, 31, 1),
    (26, 27, 1),
    (26, 32, 2),
    (27, 28, 1),
    (27, 37, 1),
    (29, 35, 1),
    (30, 36, 1),
    (33, 34, 2),
    (35, 36, 1),
    (36, 37, 2),
    (37, 38, 2)
 ),
            "explanation": "medium+, 9x13"
        },
        {
            "input": [(
    (2, 0, 0, 1, 0, 3, 0, 4, 0, 2),
    (0, 0, 3, 0, 3, 0, 0, 0, 2, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 2),
    (4, 0, 4, 0, 0, 2, 0, 4, 0, 0),
    (0, 3, 0, 0, 4, 0, 2, 0, 3, 0),
    (0, 0, 0, 0, 0, 1, 0, 3, 0, 3),
    (2, 0, 1, 0, 3, 0, 3, 0, 2, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 0, 0, 1, 0, 3, 0, 4),
    (4, 0, 5, 0, 5, 0, 1, 0, 2, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 3),
    (3, 0, 1, 0, 0, 1, 0, 2, 0, 0),
    (0, 2, 0, 0, 3, 0, 2, 0, 3, 0),
    (3, 0, 3, 0, 0, 3, 0, 3, 0, 3)
)],
            "answer": (
    (1, 2, 1),
    (1, 11, 1),
    (3, 4, 1),
    (3, 13, 2),
    (4, 5, 1),
    (4, 14, 2),
    (5, 10, 1),
    (6, 7, 1),
    (6, 12, 2),
    (7, 16, 2),
    (8, 18, 2),
    (9, 17, 1),
    (10, 21, 1),
    (11, 12, 2),
    (11, 22, 1),
    (14, 20, 2),
    (15, 16, 1),
    (15, 27, 2),
    (16, 17, 1),
    (18, 26, 1),
    (19, 20, 1),
    (21, 30, 2),
    (22, 31, 1),
    (23, 32, 1),
    (24, 25, 2),
    (24, 33, 1),
    (25, 26, 1),
    (28, 29, 1),
    (29, 30, 1),
    (29, 41, 1),
    (30, 37, 1),
    (31, 32, 1),
    (31, 38, 2),
    (32, 33, 2),
    (32, 39, 1),
    (33, 34, 1),
    (33, 43, 1),
    (35, 45, 2),
    (36, 42, 1),
    (37, 50, 2),
    (38, 46, 1),
    (40, 41, 1),
    (42, 43, 1),
    (43, 44, 1),
    (44, 45, 1),
    (46, 47, 2),
    (47, 48, 1),
    (48, 49, 2),
    (49, 50, 1)
 ),
            "explanation": "medium+, 10x14"
        },
        {
            "input": [(
    (2, 0, 2, 0, 0, 0, 3, 0, 3),
    (0, 2, 0, 0, 3, 0, 0, 3, 0),
    (3, 0, 0, 0, 0, 1, 0, 0, 3),
    (0, 3, 0, 2, 0, 0, 0, 2, 0),
    (4, 0, 3, 0, 2, 0, 0, 0, 3),
    (0, 3, 0, 2, 0, 3, 0, 3, 0),
    (3, 0, 0, 0, 0, 0, 2, 0, 4),
    (0, 3, 0, 0, 3, 0, 0, 1, 0),
    (3, 0, 2, 0, 0, 0, 4, 0, 5),
    (0, 2, 0, 0, 0, 5, 0, 2, 0),
    (3, 0, 3, 0, 2, 0, 3, 0, 2),
    (0, 2, 0, 0, 0, 3, 0, 0, 0),
    (3, 0, 0, 3, 0, 0, 6, 0, 2)
)],
            "answer": (
    (1, 8, 2),
    (2, 3, 2),
    (3, 4, 1),
    (4, 10, 2),
    (5, 6, 1),
    (5, 11, 1),
    (6, 7, 2),
    (7, 13, 1),
    (8, 14, 1),
    (9, 20, 1),
    (10, 17, 1),
    (11, 12, 2),
    (13, 21, 1),
    (14, 15, 2),
    (14, 22, 1),
    (15, 16, 1),
    (16, 26, 1),
    (17, 24, 2),
    (18, 19, 2),
    (18, 25, 1),
    (20, 21, 1),
    (20, 33, 1),
    (21, 27, 1),
    (22, 28, 2),
    (23, 30, 2),
    (24, 31, 2),
    (25, 26, 1),
    (25, 32, 1),
    (26, 37, 1),
    (28, 35, 1),
    (29, 36, 2),
    (30, 31, 2),
    (31, 39, 1),
    (32, 40, 1),
    (33, 34, 2),
    (33, 41, 2),
    (35, 42, 2),
    (36, 37, 1),
    (38, 39, 1),
    (38, 44, 2),
    (40, 41, 1),
    (42, 43, 1),
    (43, 44, 2),
    (44, 45, 2)
 ),
            "explanation": "hard, 9x13"
        },
        {
            "input": [(
    (3, 0, 2, 0, 3, 0, 0, 3, 0, 2),
    (0, 2, 0, 3, 0, 0, 0, 0, 0, 0),
    (3, 0, 0, 0, 3, 0, 2, 0, 2, 0),
    (0, 0, 0, 2, 0, 1, 0, 2, 0, 0),
    (0, 3, 0, 0, 5, 0, 2, 0, 0, 3),
    (4, 0, 0, 0, 0, 2, 0, 4, 0, 0),
    (0, 0, 2, 0, 5, 0, 2, 0, 0, 3),
    (0, 3, 0, 3, 0, 2, 0, 4, 0, 0),
    (3, 0, 2, 0, 0, 0, 0, 0, 3, 0),
    (0, 3, 0, 0, 3, 0, 0, 4, 0, 3),
    (2, 0, 0, 2, 0, 2, 0, 0, 2, 0),
    (0, 0, 3, 0, 2, 0, 0, 3, 0, 3),
    (0, 3, 0, 0, 0, 3, 0, 0, 0, 0),
    (3, 0, 0, 3, 0, 0, 0, 3, 0, 1)
)],
            "answer": (
    (1, 2, 2),
    (1, 8, 1),
    (3, 4, 2),
    (3, 9, 1),
    (4, 5, 1),
    (5, 18, 1),
    (6, 7, 1),
    (6, 15, 1),
    (7, 12, 2),
    (8, 19, 2),
    (9, 10, 1),
    (9, 16, 1),
    (10, 11, 1),
    (11, 32, 1),
    (13, 14, 1),
    (14, 21, 1),
    (15, 16, 1),
    (15, 26, 1),
    (16, 17, 2),
    (16, 23, 1),
    (18, 25, 2),
    (19, 30, 2),
    (20, 21, 2),
    (21, 29, 1),
    (22, 23, 2),
    (23, 24, 2),
    (25, 36, 1),
    (26, 27, 1),
    (26, 33, 1),
    (27, 38, 2),
    (28, 29, 2),
    (29, 35, 1),
    (30, 37, 1),
    (31, 41, 2),
    (32, 40, 2),
    (33, 45, 2),
    (34, 35, 2),
    (34, 42, 1),
    (35, 43, 1),
    (36, 44, 2),
    (37, 47, 1),
    (39, 46, 2),
    (41, 42, 1),
    (43, 44, 1),
    (43, 49, 1),
    (45, 46, 1),
    (47, 48, 2),
    (48, 49, 1),
    (49, 50, 1)
 ),
            "explanation": "hard, 10x14"
        },
    ]
}
