let state = {
    editingId: null,
    students: [],
}
export function setState(newState) {
    state = { ...state, ...newState };
}
export function getState() {
    return state;
}