import {
  createSlice,
  createAsyncThunk,
} from "@reduxjs/toolkit";

import { getAllCourses } from "../api/courseApi";

export const fetchAllCourses = createAsyncThunk(
  "courses/fetchAll",
  async () => {
    return await getAllCourses();
  }
);

const initialState = {
  courses: [],
  loading: false,
  error: null,
};

const coursesSlice = createSlice({
  name: "courses",
  initialState,

  reducers: {},

  extraReducers: (builder) => {
    builder

      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
      })

      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })

      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export default coursesSlice.reducer;

// Selectors

export const selectCourses = (state) =>
  state.courses.courses;

export const selectLoading = (state) =>
  state.courses.loading;

export const selectError = (state) =>
  state.courses.error;