import { describe, test, expect } from "vitest";
import App from "../App.jsx";

describe("smoke", () => {
  test("App loads", () => {
    expect(App).toBeTruthy();
  });
});