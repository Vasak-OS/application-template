import { createI18n } from 'vue-i18n';
import { nextTick } from 'vue';
import es from '@/locales/es.json';
import en from '@/locales/en.json';
import it from '@/locales/it.json';
import pt from '@/locales/pt.json';

let i18n: ReturnType<typeof createI18n>;

export const SUPPORT_LOCALES: Array<string> = ['es', 'en', 'pt', 'it'];

export function setI18nLanguage(locale: string): Promise<void> {
  i18n.global.locale = { value: locale };
  document.querySelector('html')?.setAttribute('lang', locale);
  localStorage.setItem('lang', locale);
  return nextTick();
}

export default function setupI18n() {
  if (!i18n) {
    const locale = localStorage.getItem('lang') || 'en';

    i18n = createI18n({
      globalInjection: true,
      legacy: false,
      locale: locale,
      mode: 'composition',
      global: true,
      fallbackLocale: 'en',
      messages: {
        es,
        en,
        it,
        pt
      }
    });
    setI18nLanguage(locale);
  }
  return i18n;
}
