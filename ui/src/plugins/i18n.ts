import { defineStore } from 'pinia';
import { computed, nextTick, ref, type Ref } from 'vue';
import es from '@/locales/es.json';
import en from '@/locales/en.json';
import it from '@/locales/it.json';
import pt from '@/locales/pt.json';

export const i18n = defineStore('i18n', () => {
  const SUPPORT_LOCALES: Array<string> = ['es', 'en', 'pt', 'it'];
  const locale: Ref<string> = ref('es');
  const messages = {
    es,
    en,
    it,
    pt
  };
  const localeMessages = computed(() => messages[locale.value]);

  function setI18nLanguage(newLocale: string): void {
    if (SUPPORT_LOCALES.indexOf(newLocale.toLocaleLowerCase()) !== -1) {
      locale.value = newLocale;
      document.querySelector('html')?.setAttribute('lang', newLocale);
      nextTick();
    }
  }

  function $t(key: string): string {
    console.info( localeMessages.value);
    return eval(`localeMessages.value.${key}.b.s`) || key;
  }

  return {
    locale,
    SUPPORT_LOCALES,
    setI18nLanguage,
    $t
  };
});
