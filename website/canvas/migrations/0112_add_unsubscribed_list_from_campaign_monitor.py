# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        unsubscribe_list = []
        
        for email in unsubscribe_list:
            print email
            orm.EmailUnsubscribe(email=email).save()


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'canvas.bestof': {
            'Meta': {'object_name': 'BestOf'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'best_of'", 'null': 'True', 'blank': 'True', 'to': "orm['canvas.Category']"}),
            'chosen_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'best_of'", 'to': "orm['canvas.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {})
        },
        'canvas.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'founded': ('django.db.models.fields.FloatField', [], {'default': '1298956320'}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'founded_categories'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'moderated_categories'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'canvas.comment': {
            'Meta': {'object_name': 'Comment'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'comments'", 'null': 'True', 'blank': 'True', 'to': "orm['canvas.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'judged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ot_hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent_comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'replies'", 'null': 'True', 'blank': 'True', 'to': "orm['canvas.Comment']"}),
            'parent_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'replied_comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['canvas.Comment']", 'null': 'True', 'blank': 'True'}),
            'reply_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'used_in_comments'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'reply_text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0', 'db_index': 'True'}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {'default': '0'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'canvas.commentflag': {
            'Meta': {'object_name': 'CommentFlag'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flags'", 'to': "orm['canvas.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'type_id': ('django.db.models.fields.IntegerField', [], {}),
            'undone': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flags'", 'to': "orm['auth.User']"})
        },
        'canvas.commentmoderationlog': {
            'Meta': {'object_name': 'CommentModerationLog'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderated_comments_log'", 'to': "orm['auth.User']"}),
            'visibility': ('django.db.models.fields.IntegerField', [], {})
        },
        'canvas.commentpin': {
            'Meta': {'object_name': 'CommentPin'},
            'auto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'canvas.commentsticker': {
            'Meta': {'object_name': 'CommentSticker'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stickers'", 'to': "orm['canvas.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'type_id': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'canvas.content': {
            'Meta': {'object_name': 'Content'},
            'alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'animated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'remix_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'remixes'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'remix_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'stamps_used': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'used_as_stamp'", 'blank': 'True', 'to': "orm['canvas.Content']"}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'url_mapping': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.ContentUrlMapping']", 'null': 'True', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'canvas.contenturlmapping': {
            'Meta': {'object_name': 'ContentUrlMapping'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'canvas.emailunsubscribe': {
            'Meta': {'object_name': 'EmailUnsubscribe'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'canvas.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fb_uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_invited': ('canvas.util.UnixTimestampField', [], {'default': '0'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'canvas.followcategory': {
            'Meta': {'object_name': 'FollowCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'followers'", 'to': "orm['canvas.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'following'", 'to': "orm['auth.User']"})
        },
        'canvas.invitecode': {
            'Meta': {'object_name': 'InviteCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitee': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'invited_from'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'inviter': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'sent_invites'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'canvas.stashcontent': {
            'Meta': {'object_name': 'StashContent'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.Content']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'canvas.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'free_invites': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_bypass': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'last_activity_check': ('canvas.util.UnixTimestampField', [], {'default': '0'}),
            'post_anonymously': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'power_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'canvas.usermoderationlog': {
            'Meta': {'object_name': 'UserModerationLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('canvas.util.UnixTimestampField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderation_log'", 'to': "orm['auth.User']"})
        },
        'canvas.userwarning': {
            'Meta': {'object_name': 'UserWarning'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['canvas.Comment']", 'null': 'True', 'blank': 'True'}),
            'confirmed': ('canvas.util.UnixTimestampField', [], {'default': '0'}),
            'custom_message': ('django.db.models.fields.TextField', [], {}),
            'disable_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued': ('canvas.util.UnixTimestampField', [], {}),
            'stock_message': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_warnings'", 'to': "orm['auth.User']"}),
            'viewed': ('canvas.util.UnixTimestampField', [], {'default': '0'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['canvas']
