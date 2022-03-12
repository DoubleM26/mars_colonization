from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.user import User
from data.departments import Department

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
# data = db_sess.query(User).filter((User.position.like("%chief%")) | (User.position.like("%middle%"))).all()
# for user in data:
#     print(f"<Colonist> {user.id} {user.surname} {user.name} {user.position}")


# db_name = input()
# global_init(db_name)
# db_sess = create_session()
# data = list(db_sess.query(Jobs).all())
# data.sort(key=lambda x: len(x.collaborators.split(", ")), reverse=True)
# max_size = 0
# team_lids = set()
# for job in data:
#     if len(job.collaborators.split(", ")) >= max_size:
#         max_size = len(job.collaborators.split(", "))
#         user = db_sess.query(User).filter(User.id == job.team_leader).first()
#         team_lids.add(user.name + " " + user.surname)
#     else:
#         break
#
# for item in team_lids:
#     print(item)


# db_name = input()
# global_init(db_name)
# db_sess = create_session()
# data = db_sess.query(Jobs).filter(User.address == "module_1", User.age < 21)
# for user in data:
#     user.address = "module_3"
#     db_sess.commit()

work_dict = {}

db_name = input()
global_init(db_name)
db_sess = create_session()
data = db_sess.query(Jobs).all()
for job in data:
    for item in job.collaborators.split(", "):
        if item not in work_dict:
            work_dict[item] = 0
        work_dict[item] += job.work_size

members = db_sess.query(Department).filter(Department.id == 1).first().members
for member in members.split(", "):
    if work_dict[member] > 25:
        user = db_sess.query(User).filter(User.id == int(member)).first()
        print(user.name + " " + user.surname)

