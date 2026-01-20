from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import BaseModel, RootModel

app = FastAPI()

# Создаём роутер с общим префиксом и тегом для Swagger
courses_router = APIRouter(
    prefix="/api/v1/courses",
    tags=["courses-service"]
)


class CourseIn(BaseModel):
    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    id: int


class CoursesStore(RootModel):
    """
    In-memory хранилище пользователей вместо реальной БД.
    """
    root: list[CourseOut]

    def find(self, id: int) -> CourseOut | None:
        """
        Находит курс по ID.
        Возвращает UserOut или None, если не найден.
        """
        return next(filter(lambda course: course.id == id, self.root), None)

    def create(self, course_in: CourseIn) -> CourseOut:
        """
        Создаёт новый курс, генерируя для него следующий ID.
        """
        course = CourseOut(id=len(self.root) + 1, **course_in.model_dump())
        self.root.append(course)
        return course

    def update(self, id: int, course_in: CourseIn) -> CourseOut:
        """
        Обновляет существующий курс по ID.
        """
        index = next(index for index, course in enumerate(self.root) if course.id == id)
        # Создаём новый объект с тем же ID и обновлёнными полями
        updated = CourseOut(id=id, **course_in.model_dump())
        # Заменяем в списке
        self.root[index] = updated
        return updated

    def delete(self, id: int) -> None:
        """
        Удаляет курс по ID, фильтруя список.
        """
        self.root = [course for course in self.root if course.id != id]


store = CoursesStore(root=[])


@courses_router.get("/{id}", response_model=CourseOut)
async def get_course(id: int):
    """
    GET /api/v1/courses/{id}
    Возвращает курс по ID или 404, если не найден.
    """
    if not (course := store.find(id)):
        raise HTTPException(
            detail=f"Course with id {id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    """
    GET /api/v1/courses
    Возвращает список всех курсов.
    """
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    """
    POST /api/v1/courses
    Создаёт новый курс и возвращает его данные с ID.
    """
    return store.create(course)


@courses_router.put("/{id}", response_model=CourseOut)
async def update_course(id: int, course: CourseIn):
    """
    PUT /api/v1/courses/{id}
    Обновляет данные курса по ID или возвращает 404, если курс не найден.
    """
    if not store.find(id):
        raise HTTPException(
            detail=f"Course with id {id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return store.update(id, course)


@courses_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(id: int):
    """
    DELETE /api/v1/courses/{id}
    Удаляет курс по ID или возвращает 404, если курс не найден.
    """
    if not store.find(id):
        raise HTTPException(
            detail=f"Course with id {id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    store.delete(id)


app.include_router(courses_router)