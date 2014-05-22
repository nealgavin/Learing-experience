#include <mysql.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static char *server_args[] = {"this_program",
							"--datadir=.",
							"--key_buffer_size=32M"};
static char server_groups[] = {"embedded",
							"server",
							"this_program_SEERVER",
							(char*)NULL};
int main()
{
	MYSQL mysql;
	MYSQL_RES *res;
	MYSQL_ROW row;
	char sqlcmd[200];
	int t,r;
	if (mysql_library_init(sizeof(server_args)/sizeof(char*),
							server_args,server_groups));
	mysql_init(&mysql);
	if (!mysql_real_connect(&mysql,"host","root","root","test",3306.NULL,0))
	{
		fprintf(stderr,"无法连接数据库，原因：%s\n",mysql_error(&mysql));

	}
	else
	{
		puts("数据库连接成功！");
		sprintf(sqlcmd,"%s",select * from call_list);
		t = mysql_real_query(&mysql,query,(unsigned int) strlen(query));
		if (t)
			printf("查询数据库失败: %s\n",mysql_error(&mysql));
		else {
			res = mysql_store_result(&mysql);
			while(row = mysql_fetch_row(res))
			{
				for(t=0;t < mysql_num_fields(res);++t)
					printf(" %s ",row[t]);
				printf("\n");
			}
			mysql_free_result(res);
		}
		mysql_close(&mysql);
	}
	mysql_library_end();
	return 0;
}
