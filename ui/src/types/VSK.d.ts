export type VSK = {
  getIcon: (string) => Promise<string>;
  loadUIConfig: () => Promise<void>;
};