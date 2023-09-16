// eslint-disable-next-line no-undef
module.exports = {
    // Emojiを非表示にするか
    disableEmoji: false,
  
    // types一覧
    // typesが設定されているのに、listに登録されてないとgit-czの実行時にエラーを吐く
    // 入れる値は、typesのvalueプロパティで指定した値
    list: [
      'contest',
      'practice',
      'updateEnv',
      'learning',
      // 'test',
      // 'feat',
      // 'fix',
      // 'chore',
      // 'docs',
      // 'refactor',
      // 'style',
      // 'ci',
      // 'perf',
      // 'config',
      // 'package',
    ],
  
    // コミットメッセージの最大文字数
    maxMessageLength: 64,
  
    // コミットメッセージの最小文字数
    minMessageLength: 3,
  
    // 質問の種類
    questions: [
      'type',
      'scope',
      'subject',
      'body',
      'breaking',
      'issues',
      'lerna',
    ],
  
    // scopesの種類
    // 一つも指定されてない場合、scopeの質問は行われなくなる
    scopes: ['atcoder'],
  
    // typesの種類を設定する
    types: {
      contest: {
        description: 'コンテストへの参加',
        emoji: '🎖️',
        value: 'コンテスト(contest)',
      },
      practice: {
        description: '開催していないコンテストの学習',
        emoji: '🏃',
        value: 'practice',
      },
      updateEnv: {
        description: '環境の更新',
        emoji: '🆙',
        value: '環境更新(updateEnv',
      },
      learning: {
        description: '勉強用',
        emoji: '📚',
        value: '勉強(learning)',
      }
    },
  }
  