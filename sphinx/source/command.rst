
コマンド
=================================


``wendy`` コマンドのヘルプを確認しましょう． ::

   $ cmd/wendy -h
   usage: WENDY [-h] [--component COMPONENT] [--entity ENTITY] [--field FIELD] [--not-delete-when-downgrade] [--host HOST] [--port PORT] action

   positional arguments:
   action                The action you want to invoke.

   optional arguments:
   -h, --help            show this help message and exit
   --component COMPONENT, -c COMPONENT
                        Name of the target component
   --entity ENTITY, -e ENTITY
                        Name of the entity
   --field FIELD, -f FIELD
                        The field to be validated
   --not-delete-when-downgrade
                        whether not to delete the migration file when downgrade
   --host HOST           host to run develop server
   --port PORT           port to run develop server



コマンド一覧
---------------

生成
^^^^^^^^^^^^^^^^^^^

ウエンディコマンドを使って，いくつかのモデルパターン，コントローラーと結合テストを生成することができます． ::

  # 生成コマンド
  $ cmd/wendy generate -c <コンポーネント名> -e <エンティティ名>
  
マイグレーション
""""""""""""""""""""
::

  $ cmd/wendy migrate

エンティティ
""""""""""""""""""""
::

  $ cmd/wendy generate -c entity -e chair

レポジトリ
""""""""""""""""""""
::

  $ cmd/wendy generate -c repository -e chair

【初期化用】シード
""""""""""""""""""""
::

  $ cmd/wendy generate -c seed -e chair

バリデータ
""""""""""""""""""""
::

  $ cmd/wendy generate -c validator -e chair

コントローラー
""""""""""""""""""""
::

  $ cmd/wendy generate -c controller -e chair

結合テスト
""""""""""""""""""""
::

  $ cmd/wendy generate -c integration_test -e chair


データベース操作
^^^^^^^^^^^^^^^^^^^

マイグレーション適用・ロールバック
""""""""""""""""""""""""""""""""
::

  $ cmd/wendy migrate:up

::

  $ cmd/wendy migrate:down

データベース初期化
"""""""""""""""""""""
::

  $ cmd/wendy seed -e chair

シェル起動
"""""""""""""""""""""
::

  $ cmd/wendy dbshell


テスト実施
^^^^^^^^^^^^^^^^^^^
::

  $ pytest -v --full-trace --cache-clear

開発サーバを立てる
^^^^^^^^^^^^^^^^^^^
::

  $ cmd/wendy run --host=0.0.0.0 --port=8000