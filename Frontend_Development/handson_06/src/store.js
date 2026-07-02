import { configureStore } from "@reduxjs/toolkit";
import enrollmentReducer from "./redux/enrollmentSlice";

export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer,
  },
});