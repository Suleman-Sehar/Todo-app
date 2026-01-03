---

description: "Task list for Add Task feature implementation"
---

# Tasks: Add Task

**Input**: Design documents from `/specs/001-add-task/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: All tasks must be implemented following the Command-Line Todo Application Constitution principles of Agentic Development Only, Spec-Driven Workflow, and Transparency & Traceability.

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Create src directory and initialize Python package
- [x] T003 [P] Create tests directory and initialize Python package

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task model in src/models.py
- [x] T005 Create utils module in src/utils.py with ID generation function
- [x] T006 Create todo module in src/todo.py with in-memory task storage
- [x] T007 Create main.py with basic CLI structure

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with a required title and optional description via the CLI

**Independent Test**: The application allows a user to add a new task via the CLI with a required title and optional description, storing it in memory and displaying a confirmation message.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [x] T008 [P] [US1] Unit test for Task model in tests/unit/test_models.py
- [x] T009 [P] [US1] Unit test for ID generation in tests/unit/test_utils.py
- [x] T010 [P] [US1] Contract test for add_task functionality in tests/contract/test_add_task.py

### Implementation for User Story 1

- [x] T011 [P] [US1] Implement Task class in src/models.py with id, title, description, is_completed
- [x] T012 [P] [US1] Implement generate_id function in src/utils.py
- [x] T013 [US1] Implement add_task function in src/todo.py
- [x] T014 [US1] Implement CLI menu with "Add Task" option in src/main.py
- [x] T015 [US1] Implement user input prompts for title and description in src/main.py
- [x] T016 [US1] Add validation for non-empty title in src/utils.py
- [x] T017 [US1] Add error handling for empty title input in src/main.py
- [x] T018 [US1] Add confirmation message after successful task creation in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T019 [P] Documentation updates in README.md
- [ ] T020 Code cleanup and refactoring
- [ ] T021 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T022 Security hardening
- [ ] T023 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task model in tests/unit/test_models.py"
Task: "Unit test for ID generation in tests/unit/test_utils.py"
Task: "Contract test for add_task functionality in tests/contract/test_add_task.py"

# Launch all models for User Story 1 together:
Task: "Implement Task class in src/models.py with id, title, description, is_completed"
Task: "Implement generate_id function in src/utils.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence